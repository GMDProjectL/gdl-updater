import os
from github import download_latest_tarball

def download_latest_installer_release(destination_file: str):
    download_latest_tarball('GMDProjectL/installer', destination_file)

    return destination_file
    
def unpack_installer(installer_tarball: str, destination_dir: str):
    return os.system(f'tar -xvf {installer_tarball} -C {destination_dir} --strip-components=1') == 0

def download_and_unpack_installer(installer_dir: str):
    tarball = download_latest_installer_release('/tmp/installer.tar.gz')

    if not os.path.exists(installer_dir):
        os.system(f'pkexec sh -c "mkdir -p {installer_dir} && chown -R 1000:1000 {installer_dir}"')
    
    os.system(f'rm -rf {installer_dir}/**')

    unpack_installer(tarball, installer_dir)

    return installer_dir

def install_dependencies(installer_dir: str):
    return os.system(f'cd {installer_dir} && pnpm install')

def build_installer(installer_dir: str):
    return os.system(f'cd {installer_dir} && pnpm build')

def download_and_deploy_installer(installer_dir: str):
    download_and_unpack_installer(installer_dir)
    install_dependencies(installer_dir)
    build_installer(installer_dir)

    return installer_dir

def run_installer_frontend(installer_dir: str):
    return os.system(f'cd {installer_dir} && pnpm preview')

def run_installer_backend(installer_dir: str):
    return os.system(f'cd {installer_dir}/python-side && pkexec --keep-cwd python3 main.py')

def run_electron_window(installer_dir: str):
    return os.system(f'cd {installer_dir} && python wait-for-node.py --update')
