import click
from pathlib import Path


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'],
                        max_content_width=80)


def create_dirs(dirs_to_create):
    for d in dirs_to_create:
        d.mkdir(mode=0o755, parents=True)


def create_files(files_to_create):
    for f in files_to_create:
        open(f, 'a').close()


def create_playbook(location):
    dirs_to_create = [
        location.joinpath('group_vars'),
        location.joinpath('roles'),
    ]
    files_to_create = [
        location.joinpath('group_vars', 'all'),
        location.joinpath('playbook.yml'),
    ]

    create_dirs(dirs_to_create)
    create_files(files_to_create)


def create_role(location, rolename):
    dirs_to_create = [
        location.joinpath("roles", rolename),
        location.joinpath("roles", rolename, "tasks"),
        location.joinpath("roles", rolename, "handlers"),
        location.joinpath("roles", rolename, "templates"),
        location.joinpath("roles", rolename, "files"),
        location.joinpath("roles", rolename, "vars"),
        location.joinpath("roles", rolename, "meta"),
    ]
    files_to_create = [
        location.joinpath("roles", rolename, "tasks", "main.yml"),
        location.joinpath("roles", rolename, "handlers", "main.yml"),
    ]

    create_dirs(dirs_to_create)
    create_files(files_to_create)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('playbook_location',
                type=click.Path(file_okay=False, dir_okay=False, resolve_path=True))
@click.argument('roles_to_create', nargs=-1)
def make_skeleton(playbook_location, roles_to_create):
    location = Path(playbook_location)
    location.mkdir(parents=True)

    click.echo(f'Creating playbook: {location.stem}')
    create_playbook(location)

    for r in roles_to_create:
        click.echo(f'... creating role: {r}')
        create_role(location, r)
