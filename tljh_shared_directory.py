from tljh.hooks import hookimpl
from tljh.user import ensure_group
import sh

@hookimpl
def tljh_extra_user_conda_packages():
    return ['voila']

@hookimpl
def tljh_config_post_install(config):
    """
    Configure /srv/scratch and change configs/mods
    """
    ### mkdir -p /srv/scratch
    ### sudo chown  root:jupyterhub-users /srv/scratch
    ### sudo chmod 777 /srv/scratch
    ### sudo chmod g+s /srv/scratch
    ### sudo ln -s /srv/scratch /etc/skel/scratch
    sh.mkdir('/srv/scratch', '-p')
    # jupyterhub-users doesn't get created until a user logs in
    # make sure it's created before changing permissions on directory
    ensure_group('jupyterhub-users') 
    sh.chown('root:jupyterhub-users', '/srv/scratch')
    sh.chmod('777', '/srv/scratch')
    sh.chmod('g+s', '/srv/scratch')
    sh.ln('-s', '/srv/scratch', '/etc/skel/scratch')

    
    
    