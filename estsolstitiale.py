#!/usr/bin/env python3

from pathlib import Path
import argparse
import logging
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass


MAX_SIZE = 10 * 1024 * 1024 * 1024  # 10 GB
PROGRAM_NAME = "Estsolstitiale"
DEFAULT_SCRIPT_NAME = "estsolstitiale.py"


@dataclass(frozen=True)
class Config:
    base: Path
    source: Path
    encrypted: Path
    decrypted: Path
    config_dir: Path
    public_key_file: Path
    private_key_file: Path
    public_key: str


def default_paths() -> dict[str, Path]:
    home = Path.home()

    base = home / "estsolstitiale"
    config_dir = base / "config"

    return {
        "home": home,
        "base": base,
        "source": base / "source",
        "encrypted": home / "OneDrive" / "encrypted",
        "decrypted": base / "decrypted",
        "config_dir": config_dir,
        "public_key_file": config_dir / "public_key.txt",
        "private_key_file": config_dir / "age_key.txt",
    }


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )


def require_command(command: str) -> None:
    if shutil.which(command) is None:
        raise RuntimeError(f"Command not found: {command}")


def ask_yes_no(question: str, default: bool = False) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"

    while True:
        answer = input(f"{question} {suffix}: ").strip().lower()

        if not answer:
            return default

        if answer in {"y", "yes"}:
            return True

        if answer in {"n", "no"}:
            return False

        print("Invalid answer. Please type yes or no.")


def validate_public_key(public_key: str) -> None:
    if not public_key:
        raise ValueError("The public key cannot be empty.")

    if not public_key.startswith("age1"):
        raise ValueError("The age public key seems invalid. It should start with 'age1'.")


def validate_private_key_file(private_key_file: Path) -> None:
    if not private_key_file.exists():
        raise FileNotFoundError(f"Private key not found: {private_key_file}")

    if not private_key_file.is_file():
        raise ValueError(f"The private key path is not a file: {private_key_file}")

    content = private_key_file.read_text(encoding="utf-8", errors="ignore")

    if "AGE-SECRET-KEY-" not in content:
        raise ValueError(
            "The file does not seem to contain a valid age private key "
            "because 'AGE-SECRET-KEY-' was not found."
        )


def derive_public_key_from_private(private_key_file: Path) -> str | None:
    if shutil.which("age-keygen") is None:
        return None

    try:
        result = subprocess.run(
            ["age-keygen", "-y", str(private_key_file)],
            check=True,
            text=True,
            capture_output=True,
        )

        public_key = result.stdout.strip()
        validate_public_key(public_key)
        return public_key

    except Exception:
        return None


def create_directories_from_paths(paths: dict[str, Path]) -> None:
    paths["base"].mkdir(parents=True, exist_ok=True)
    paths["source"].mkdir(parents=True, exist_ok=True)
    paths["encrypted"].mkdir(parents=True, exist_ok=True)
    paths["decrypted"].mkdir(parents=True, exist_ok=True)
    paths["config_dir"].mkdir(parents=True, exist_ok=True)


def configuration_exists() -> bool:
    paths = default_paths()

    return (
        paths["public_key_file"].exists()
        and paths["private_key_file"].exists()
    )


def first_setup(force: bool = False) -> None:
    paths = default_paths()

    print(
        """
==============================
Estsolstitiale Configuration
==============================
"""
    )

    print("Directories used:")
    print(f"- Base      : {paths['base']}")
    print(f"- Source    : {paths['source']}")
    print(f"- Encrypted : {paths['encrypted']}")
    print(f"- Decrypted : {paths['decrypted']}")
    print(f"- Config    : {paths['config_dir']}")
    print()

    if configuration_exists() and not force:
        print("Configuration already exists.")
        print("If you want to configure again, use:")
        print("python3 estsolstitiale.py setup --force")
        return

    if force and configuration_exists():
        confirm = ask_yes_no(
            "A configuration already exists. Do you want to overwrite it?",
            default=False,
        )

        if not confirm:
            print("Configuration cancelled.")
            return

    create_directories_from_paths(paths)

    public_key_file = paths["public_key_file"]
    private_key_file = paths["private_key_file"]

    print("Step 1: age private key")
    print()
    print("You need to provide the path to your existing age private key.")
    print("Common example: ~/.config/age/key.txt")
    print()

    while True:
        private_key_input = input("Path to the age private key: ").strip()

        if not private_key_input:
            print("The path cannot be empty.")
            continue

        source_private_key = Path(private_key_input).expanduser()

        try:
            validate_private_key_file(source_private_key)
            break
        except Exception as exc:
            print(f"Error: {exc}")

    if source_private_key.resolve() != private_key_file.resolve():
        if private_key_file.exists():
            private_key_file.unlink()

        shutil.copy2(source_private_key, private_key_file)

    try:
        private_key_file.chmod(0o600)
    except OSError:
        pass

    print()
    print("Step 2: age public key")
    print()

    detected_public_key = derive_public_key_from_private(private_key_file)

    if detected_public_key:
        print("Public key automatically detected from the private key:")
        print(detected_public_key)
        print()

        use_detected = ask_yes_no("Use this public key?", default=True)

        if use_detected:
            public_key = detected_public_key
        else:
            public_key = input("Paste your age public key: ").strip()
    else:
        print("Could not automatically detect the public key.")
        print("Please paste it manually.")
        print()
        public_key = input("Age public key: ").strip()

    validate_public_key(public_key)

    public_key_file.write_text(public_key + "\n", encoding="utf-8")

    print(
        f"""
Configuration completed successfully.

Files created:
- {public_key_file}
- {private_key_file}

Directories ready:
- {paths['source']}
- {paths['encrypted']}
- {paths['decrypted']}

You can now run:
python3 estsolstitiale.py

Or directly:
python3 estsolstitiale.py encrypt
"""
    )


def reset_config() -> None:
    paths = default_paths()
    config_dir = paths["config_dir"]

    print(
        """
==============================
Reset Configuration
==============================
"""
    )

    if not config_dir.exists():
        print("No configuration found.")
        return

    print(f"Configuration found: {config_dir}")
    confirm = ask_yes_no("Delete the entire Estsolstitiale configuration?", default=False)

    if not confirm:
        print("Reset cancelled.")
        return

    shutil.rmtree(config_dir)
    print("Configuration deleted.")


def load_config() -> Config:
    paths = default_paths()

    base = paths["base"]
    source = paths["source"]
    encrypted = paths["encrypted"]
    decrypted = paths["decrypted"]
    config_dir = paths["config_dir"]
    public_key_file = paths["public_key_file"]
    private_key_file = paths["private_key_file"]

    if not public_key_file.exists():
        raise FileNotFoundError(f"Public key not found: {public_key_file}")

    if not private_key_file.exists():
        raise FileNotFoundError(f"Private key not found: {private_key_file}")

    public_key = public_key_file.read_text(encoding="utf-8").strip()

    validate_public_key(public_key)
    validate_private_key_file(private_key_file)

    return Config(
        base=base,
        source=source,
        encrypted=encrypted,
        decrypted=decrypted,
        config_dir=config_dir,
        public_key_file=public_key_file,
        private_key_file=private_key_file,
        public_key=public_key,
    )


def ensure_directories(config: Config) -> None:
    config.source.mkdir(parents=True, exist_ok=True)
    config.encrypted.mkdir(parents=True, exist_ok=True)
    config.decrypted.mkdir(parents=True, exist_ok=True)
    config.config_dir.mkdir(parents=True, exist_ok=True)


def encrypted_to_original_path(config: Config, encrypted_file: Path) -> Path:
    rel = encrypted_file.relative_to(config.encrypted)

    if rel.suffix != ".age":
        raise ValueError(f"Unexpected non-age file: {encrypted_file}")

    original_rel = rel.with_suffix("")
    return config.source / original_rel


def encrypted_to_decrypted_path(config: Config, encrypted_file: Path) -> Path:
    rel = encrypted_file.relative_to(config.encrypted)

    if rel.suffix != ".age":
        raise ValueError(f"Unexpected non-age file: {encrypted_file}")

    out_rel = rel.with_suffix("")
    return config.decrypted / out_rel


def should_update(src: Path, dst: Path) -> bool:
    if not dst.exists():
        return True

    return src.stat().st_mtime > dst.stat().st_mtime


def run_command(command: list[str], dry_run: bool = False) -> bool:
    logging.debug("Command: %s", " ".join(command))

    if dry_run:
        logging.info("[dry-run] %s", " ".join(command))
        return True

    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as exc:
        logging.error(
            "Command failed with code %s: %s",
            exc.returncode,
            " ".join(command),
        )
        return False


def encrypt_file(src: Path, dst: Path, public_key: str, dry_run: bool = False) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)

    tmp = dst.with_name(dst.name + ".tmp")

    logging.info("Encrypting: %s", src)

    if dry_run:
        logging.info("[dry-run] would write: %s", dst)
        return True

    if tmp.exists():
        tmp.unlink()

    success = run_command(
        [
            "age",
            "-r",
            public_key,
            "-o",
            str(tmp),
            str(src),
        ],
        dry_run=False,
    )

    if not success:
        if tmp.exists():
            tmp.unlink()
        return False

    tmp.replace(dst)
    return True


def decrypt_file(src: Path, dst: Path, private_key: Path, dry_run: bool = False) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)

    tmp = dst.with_name(dst.name + ".tmp")

    logging.info("Decrypting: %s", src)

    if dry_run:
        logging.info("[dry-run] would write: %s", dst)
        return True

    if tmp.exists():
        tmp.unlink()

    success = run_command(
        [
            "age",
            "-d",
            "-i",
            str(private_key),
            "-o",
            str(tmp),
            str(src),
        ],
        dry_run=False,
    )

    if not success:
        if tmp.exists():
            tmp.unlink()
        return False

    tmp.replace(dst)
    return True


def remove_empty_dirs(path: Path, dry_run: bool = False) -> None:
    if not path.exists():
        return

    for root, dirs, files in os.walk(path, topdown=False):
        root_path = Path(root)

        if root_path == path:
            continue

        try:
            if not any(root_path.iterdir()):
                logging.info("Empty directory: %s", root_path)

                if not dry_run:
                    root_path.rmdir()
        except OSError as exc:
            logging.warning("Could not remove directory %s: %s", root_path, exc)


def encrypt_sync(config: Config, dry_run: bool = False, upload: bool = True) -> None:
    logging.info("Synchronizing source -> encrypted")

    encrypted_count = 0
    skipped_count = 0
    error_count = 0

    for src in config.source.rglob("*"):
        if not src.is_file():
            continue

        size = src.stat().st_size

        if size > MAX_SIZE:
            logging.warning("Too large, skipped: %s", src)
            skipped_count += 1
            continue

        rel = src.relative_to(config.source)
        dst = config.encrypted / rel.with_name(rel.name + ".age")

        if should_update(src, dst):
            ok = encrypt_file(src, dst, config.public_key, dry_run=dry_run)

            if ok:
                encrypted_count += 1
            else:
                error_count += 1

    logging.info("Removing orphan encrypted files")

    for enc in config.encrypted.rglob("*.age"):
        original = encrypted_to_original_path(config, enc)

        if not original.exists():
            logging.info("Removing orphan: %s", enc)

            if not dry_run:
                enc.unlink()

    remove_empty_dirs(config.encrypted, dry_run=dry_run)

    logging.info(
        "Encryption completed: %s file(s), %s skipped, %s error(s)",
        encrypted_count,
        skipped_count,
        error_count,
    )

    if upload:
        logging.info("Uploading to OneDrive")
        run_command(["onedrive", "--synchronize", "--verbose"], dry_run=dry_run)

    logging.info("Encrypt sync completed")


def decrypt_sync(config: Config, dry_run: bool = False, clean_orphans: bool = True) -> None:
    logging.info("Synchronizing encrypted -> decrypted")

    decrypted_count = 0
    skipped_count = 0
    error_count = 0

    for enc in config.encrypted.rglob("*.age"):
        out = encrypted_to_decrypted_path(config, enc)

        if not should_update(enc, out):
            skipped_count += 1
            continue

        ok = decrypt_file(enc, out, config.private_key_file, dry_run=dry_run)

        if ok:
            decrypted_count += 1
        else:
            error_count += 1

    if clean_orphans:
        logging.info("Removing orphan decrypted files")

        for out in config.decrypted.rglob("*"):
            if not out.is_file():
                continue

            rel = out.relative_to(config.decrypted)
            enc = config.encrypted / rel.with_name(rel.name + ".age")

            if not enc.exists():
                logging.info("Removing orphan: %s", out)

                if not dry_run:
                    out.unlink()

        remove_empty_dirs(config.decrypted, dry_run=dry_run)

    logging.info(
        "Decryption completed: %s file(s), %s skipped, %s error(s)",
        decrypted_count,
        skipped_count,
        error_count,
    )


def interactive_menu(config: Config) -> None:
    while True:
        print(
            """
========================
Estsolstitiale
========================
1. Encrypt, sync and upload
2. Sync and decrypt
3. Dry-run encrypt
4. Dry-run decrypt
5. Reconfigure
6. Exit
"""
        )

        choice = input("Select option: ").strip()

        if choice == "1":
            encrypt_sync(config)

        elif choice == "2":
            decrypt_sync(config)

        elif choice == "3":
            encrypt_sync(config, dry_run=True, upload=False)

        elif choice == "4":
            decrypt_sync(config, dry_run=True)

        elif choice == "5":
            first_setup(force=True)
            config = load_config()
            ensure_directories(config)

        elif choice == "6":
            return

        else:
            print("Invalid option.")



def script_name() -> str:
    """Return the current script name, with the README name as a friendly fallback."""
    current = Path(sys.argv[0]).name
    return current if current else DEFAULT_SCRIPT_NAME


def open_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if sys.platform.startswith("linux"):
        subprocess.Popen(["xdg-open", str(path)])
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(path)])
    elif os.name == "nt":
        os.startfile(path)  # type: ignore[attr-defined]
    else:
        raise RuntimeError(f"Cannot open directories automatically on this platform: {sys.platform}")


def gui_setup(parent=None, force: bool = False) -> bool:
    """Small Tkinter setup wizard matching the CLI configuration files."""
    try:
        from tkinter import filedialog, messagebox, simpledialog
    except Exception as exc:
        raise RuntimeError(f"Tkinter is not available: {exc}") from exc

    paths = default_paths()
    if configuration_exists() and not force:
        overwrite = messagebox.askyesno(
            PROGRAM_NAME,
            "A configuration already exists. Do you want to reconfigure it?",
            parent=parent,
        )
        if not overwrite:
            return False
        force = True

    if force and configuration_exists():
        overwrite = messagebox.askyesno(
            PROGRAM_NAME,
            "This will overwrite the stored public and private key copy. Continue?",
            parent=parent,
        )
        if not overwrite:
            return False

    create_directories_from_paths(paths)
    private_key_file = paths["private_key_file"]
    public_key_file = paths["public_key_file"]

    selected = filedialog.askopenfilename(
        parent=parent,
        title="Select your age private key",
        initialdir=str(Path.home()),
    )
    if not selected:
        return False

    source_private_key = Path(selected).expanduser()
    validate_private_key_file(source_private_key)

    if source_private_key.resolve() != private_key_file.resolve():
        if private_key_file.exists():
            private_key_file.unlink()
        shutil.copy2(source_private_key, private_key_file)
    try:
        private_key_file.chmod(0o600)
    except OSError:
        pass

    detected_public_key = derive_public_key_from_private(private_key_file)
    public_key = None
    if detected_public_key:
        use_detected = messagebox.askyesno(
            PROGRAM_NAME,
            "Public key automatically detected from the private key:\n\n"
            f"{detected_public_key}\n\nUse this public key?",
            parent=parent,
        )
        if use_detected:
            public_key = detected_public_key

    if not public_key:
        public_key = simpledialog.askstring(
            PROGRAM_NAME,
            "Paste your age public key:",
            parent=parent,
        )
        if public_key is None:
            return False
        public_key = public_key.strip()

    validate_public_key(public_key)
    public_key_file.write_text(public_key + "\n", encoding="utf-8")
    messagebox.showinfo(
        PROGRAM_NAME,
        "Configuration completed successfully.\n\n"
        f"Source: {paths['source']}\n"
        f"Encrypted: {paths['encrypted']}\n"
        f"Decrypted: {paths['decrypted']}",
        parent=parent,
    )
    return True


def start_gui() -> None:
    """Start the ultra-lightweight Tkinter GUI described in the README."""
    try:
        import queue
        import threading
        import tkinter as tk
        from tkinter import messagebox, scrolledtext
    except Exception as exc:
        raise RuntimeError(f"Tkinter is not available: {exc}") from exc

    class QueueLogHandler(logging.Handler):
        def __init__(self, log_queue):
            super().__init__()
            self.log_queue = log_queue
            self.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

        def emit(self, record):
            self.log_queue.put(self.format(record))

    root = tk.Tk()
    root.title(PROGRAM_NAME)
    root.geometry("820x520")

    log_queue = queue.Queue()
    queue_handler = QueueLogHandler(log_queue)
    logging.getLogger().addHandler(queue_handler)

    main_frame = tk.Frame(root, padx=12, pady=12)
    main_frame.pack(fill="both", expand=True)

    title = tk.Label(main_frame, text=PROGRAM_NAME, font=("TkDefaultFont", 18, "bold"))
    title.pack(anchor="w")

    subtitle = tk.Label(
        main_frame,
        text="Privacy-oriented encrypted synchronization helper for OneDrive",
    )
    subtitle.pack(anchor="w", pady=(0, 12))

    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill="x", pady=(0, 10))

    log_box = scrolledtext.ScrolledText(main_frame, height=18, state="disabled")
    log_box.pack(fill="both", expand=True)

    def append_log(message: str) -> None:
        log_box.configure(state="normal")
        log_box.insert("end", message + "\n")
        log_box.see("end")
        log_box.configure(state="disabled")

    def poll_logs() -> None:
        while True:
            try:
                append_log(log_queue.get_nowait())
            except queue.Empty:
                break
        root.after(150, poll_logs)

    def run_background(label: str, target, *args, **kwargs) -> None:
        def worker() -> None:
            logging.info("Starting: %s", label)
            try:
                target(*args, **kwargs)
                logging.info("Completed: %s", label)
            except Exception as exc:
                logging.error("%s failed: %s", label, exc)
                root.after(0, lambda: messagebox.showerror(PROGRAM_NAME, str(exc), parent=root))
        threading.Thread(target=worker, daemon=True).start()

    def with_config(action, *args, **kwargs):
        config = load_config()
        ensure_directories(config)
        return action(config, *args, **kwargs)

    def setup_action() -> None:
        try:
            if gui_setup(parent=root, force=True):
                logging.info("Configuration completed.")
        except Exception as exc:
            logging.error("Setup failed: %s", exc)
            messagebox.showerror(PROGRAM_NAME, str(exc), parent=root)

    def open_path(kind: str) -> None:
        paths = default_paths()
        open_directory(paths[kind])

    buttons = [
        ("Encrypt + Sync", lambda: run_background("Encrypt + Sync", with_config, encrypt_sync)),
        ("Decrypt", lambda: run_background("Decrypt", with_config, decrypt_sync)),
        ("Dry Encrypt", lambda: run_background("Dry Encrypt", with_config, encrypt_sync, True, False)),
        ("Dry Decrypt", lambda: run_background("Dry Decrypt", with_config, decrypt_sync, True)),
        ("Setup", setup_action),
        ("Open Source", lambda: open_path("source")),
        ("Open Encrypted", lambda: open_path("encrypted")),
        ("Open Decrypted", lambda: open_path("decrypted")),
    ]

    for index, (text, command) in enumerate(buttons):
        tk.Button(button_frame, text=text, command=command, width=18).grid(
            row=index // 4,
            column=index % 4,
            padx=4,
            pady=4,
            sticky="ew",
        )

    if not configuration_exists():
        append_log("No configuration found. Click Setup to configure Estsolstitiale.")
    else:
        append_log("Configuration found. Ready.")

    poll_logs()
    root.mainloop()

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estsolstitiale encrypted OneDrive synchronizer"
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=["gui", "cli", "menu", "encrypt", "decrypt", "setup", "reset-config"],
        default="gui",
        help="Action to run",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate actions without modifying files",
    )

    parser.add_argument(
        "--no-upload",
        action="store_true",
        help="Do not run OneDrive synchronization after encryption",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable detailed logs",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Force reconfiguration",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(verbose=args.verbose)

    try:
        require_command("age")

        if args.command == "setup":
            first_setup(force=args.force)
            return 0

        if args.command == "reset-config":
            reset_config()
            return 0

        if args.command == "gui":
            start_gui()
            return 0

        if not configuration_exists():
            print("First use detected.")
            first_setup(force=False)

        if args.command == "encrypt" and not args.no_upload:
            require_command("onedrive")

        config = load_config()
        ensure_directories(config)

        if args.command in {"cli", "menu"}:
            interactive_menu(config)

        elif args.command == "encrypt":
            if not args.no_upload:
                require_command("onedrive")

            encrypt_sync(
                config,
                dry_run=args.dry_run,
                upload=not args.no_upload,
            )

        elif args.command == "decrypt":
            decrypt_sync(
                config,
                dry_run=args.dry_run,
            )

        return 0

    except KeyboardInterrupt:
        logging.warning("Interrupted by user.")
        return 130

    except Exception as exc:
        logging.error("Error: %s", exc)
        return 1

if __name__ == "__main__":
    sys.exit(main())