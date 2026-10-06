import customtkinter as ctk
import threading
from src.main import recover_rct3, restore_rct3
from src.diagnostics import (
    find_steam,
    find_steam_libraries,
    find_rct3,
    hash_file,
    identify_build,
)


ctk.set_appearance_mode("dark")


class RCT3CompatibilityHelper(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("RCT3 Compatibility Helper")
        self.geometry("600x450")
        self.resizable(False, False)

        self.create_widgets()
        self.detect_game()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="🎢 RCT3 Compatibility Helper",
            font=ctk.CTkFont(size=26, weight="bold"),
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="RollerCoaster Tycoon 3 Complete Edition",
            font=ctk.CTkFont(size=14),
        )
        self.subtitle_label.pack(pady=(0, 25))

        self.status_frame = ctk.CTkFrame(self)
        self.status_frame.pack(
            padx=40,
            pady=10,
            fill="x",
        )

        self.steam_status = ctk.CTkLabel(
            self.status_frame,
            text="Checking Steam...",
            anchor="w",
        )
        self.steam_status.pack(
            padx=20,
            pady=(20, 5),
            fill="x",
        )

        self.game_status = ctk.CTkLabel(
            self.status_frame,
            text="Checking RCT3...",
            anchor="w",
        )
        self.game_status.pack(
            padx=20,
            pady=5,
            fill="x",
        )

        self.build_status = ctk.CTkLabel(
            self.status_frame,
            text="Checking game version...",
            anchor="w",
        )
        self.build_status.pack(
            padx=20,
            pady=(5, 20),
            fill="x",
        )

        self.message_label = ctk.CTkLabel(
            self,
            text="",
            wraplength=500,
            justify="center",
        )
        self.message_label.pack(
            padx=40,
            pady=20,
        )

        self.fix_button = ctk.CTkButton(
            self,
            text="Install Compatibility Fix",
            command=self.start_recovery,
            state="disabled",
        )
        self.fix_button.pack(
            padx=40,
            pady=(10, 5),
        )

        self.restore_button = ctk.CTkButton(
            self,
            text="Restore Original Version",
            command=self.start_restore,
            state="disabled",
        )
        self.restore_button.pack(
            padx=40,
            pady=(5, 10),
        )

    def detect_game(self):
        steam_path = find_steam()

        if steam_path is None:
            self.steam_status.configure(
                text="✕ Steam not found"
            )
            self.game_status.configure(
                text="— RCT3 not checked"
            )
            self.build_status.configure(
                text="— Version not checked"
            )
            self.message_label.configure(
                text="Steam could not be found on this computer."
            )
            return

        self.steam_status.configure(
            text="✓ Steam found"
        )

        libraries = find_steam_libraries(steam_path)
        rct3_path = find_rct3(libraries)

        if rct3_path is None:
            self.game_status.configure(
                text="✕ RCT3 installation not found"
            )
            self.build_status.configure(
                text="— Version not checked"
            )
            self.message_label.configure(
                text=(
                    "RollerCoaster Tycoon 3 Complete Edition "
                    "could not be found."
                )
            )
            return

        self.game_status.configure(
            text="✓ RCT3 installation found"
        )

        game_hash = hash_file(rct3_path)
        game_build = identify_build(game_hash)

        if game_build == "current":
            self.build_status.configure(
                text="⚠ Affected version detected"
            )

            self.message_label.configure(
                text=(
                    "This version of RCT3 may crash when saving "
                    "Peep Designer groups. The compatibility fix "
                    "can install a verified earlier executable."
                )
            )

            self.fix_button.configure(
                text="Install Compatibility Fix",
                state="normal"
            )
            self.restore_button.configure(
                text="Restore Original Version",
                state="disabled"
            )

        elif game_build == "legacy":
            self.build_status.configure(
                text="✓ Compatibility version installed"
            )

            self.message_label.configure(
                text=(
                    "The known-working compatibility version "
                    "is already installed."
                )
            )

            self.fix_button.configure(
                text="Compatibility Fix Installed",
                state="disabled"
            )
            self.restore_button.configure(
                text="Restore Original Version",
                state="normal"
            )

        else:
            self.build_status.configure(
                text="⚠ Unknown RCT3 version"
            )

            self.message_label.configure(
                text=(
                    "This RCT3 executable is not recognized. "
                    "No changes will be made."
                )
            )

            self.fix_button.configure(state="disabled")
            self.restore_button.configure(state="disabled")

    def start_recovery(self):
        self.fix_button.configure(
            text="Installing...",
            state="disabled"
        )
        self.restore_button.configure(state="disabled")
        self.message_label.configure(
            text=(
                "Preparing the compatibility fix. "
                "Steam QR authentication may open shortly."
            )
        )

        threading.Thread(
            target=self.run_recovery,
            daemon=True,
        ).start()

    def run_recovery(self):
        try:
            success, message = recover_rct3()
        except Exception as error:
            success = False
            message = f"Compatibility fix failed: {error}"

        self.after(
            0,
            self.finish_recovery,
            success,
            message,
        )

    def finish_recovery(self, success, message):
        self.message_label.configure(text=message)

        if success:
            # Re-detect instead of assuming what the backend installed.
            self.detect_game()
        else:
            self.fix_button.configure(
                text="Try Again",
                state="normal",
            )

    def start_restore(self):
        self.restore_button.configure(
            text="Restoring...",
            state="disabled"
        )
        self.fix_button.configure(state="disabled")
        self.message_label.configure(
            text="Restoring the verified original RCT3 executable..."
        )

        threading.Thread(
            target=self.run_restore,
            daemon=True,
        ).start()

    def run_restore(self):
        try:
            success, message = restore_rct3()
        except Exception as error:
            success = False
            message = f"Restore failed: {error}"

        self.after(
            0,
            self.finish_restore,
            success,
            message,
        )

    def finish_restore(self, success, message):
        self.message_label.configure(text=message)

        if success:
            # Re-detect so the UI reflects the executable actually on disk.
            self.detect_game()
        else:
            self.restore_button.configure(
                text="Restore Original Version",
                state="normal",
            )


if __name__ == "__main__":
    print("Yoan I love you 💖")
    app = RCT3CompatibilityHelper()
    app.mainloop()