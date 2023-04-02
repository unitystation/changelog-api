from .models import BuildVersion, Change

def add_version_to_unversioned_changes():
    latest_build = get_latest_version()
    unversioned_changes = get_unversioned_changes()

    for change in unversioned_changes:
        change.build = latest_build
        change.date_added = latest_build.date_created
        change.save()


def get_latest_version() -> BuildVersion | None:
    return BuildVersion.objects.first()


def get_unversioned_changes() -> list[Change]:
    return Change.objects.filter(build=None)


def get_latest_stable_version() -> BuildVersion | None:
    return BuildVersion.objects.filter(is_stable=True).first()