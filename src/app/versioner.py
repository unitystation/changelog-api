from .models import BuildVersion, Change

def add_version_to_unversioned_changes():
    latest_build = _get_latest_version()
    unversioned_changes = get_unversioned_changes()

    for change in unversioned_changes:
        change.build = latest_build
        change.date_added = latest_build.date_created
        change.save()

def _get_latest_version() -> BuildVersion:
    return BuildVersion.objects.latest('date_created')

def get_unversioned_changes() -> list[Change]:
    return Change.objects.filter(build=None)