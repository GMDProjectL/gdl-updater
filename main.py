from update import download_and_deploy_installer, run_installer_backend, run_installer_frontend, run_electron_window
from threading import Thread

installer_dir = '/opt/installer'
download_and_deploy_installer(installer_dir)

backend_thread = Thread(target=run_installer_backend, args=(installer_dir,))
backend_thread.start()

frontend_thread = Thread(target=run_installer_frontend, args=(installer_dir,))
frontend_thread.start()

run_electron_window(installer_dir)
print("Done, leaving")
exit(0)