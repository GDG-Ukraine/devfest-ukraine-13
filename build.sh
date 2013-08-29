#!/bin/sh

APP_DIR=$1
BUILD_DIR='./build'

die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "APP_DIR argument required"
[ -d "$1" ] || die "Directory $1 does not exist"

which git
[ $? -eq 0 ] || die "No git installed"
which hg
[ $? -eq 0 ] || die "No mercurial (hg) installed"

mkdir $BUILD_DIR

pip install --download=$BUILD_DIR --no-install -r requirements.txt

### Django-nonrel
unzip -q $BUILD_DIR/django-autoload-*.zip -d $BUILD_DIR
unzip -q $BUILD_DIR/django-dbindexer-*.zip -d $BUILD_DIR
unzip -q $BUILD_DIR/django-nonrel-1.4.5.zip -d $BUILD_DIR
unzip -q $BUILD_DIR/djangoappengine-1.*.zip -d $BUILD_DIR
unzip -q $BUILD_DIR/djangotoolbox-*.zip -d $BUILD_DIR

cp -r $BUILD_DIR/django-autoload/autoload $APP_DIR/autoload
cp -r $BUILD_DIR/django-dbindexer/dbindexer $APP_DIR/dbindexer
cp -r $BUILD_DIR/django-nonrel/django $APP_DIR/django
cp -r $BUILD_DIR/djangoappengine/djangoappengine $APP_DIR/djangoappengine
cp -r $BUILD_DIR/djangotoolbox/djangotoolbox $APP_DIR/djangotoolbox
# others...


rm -rI $BUILD_DIR
