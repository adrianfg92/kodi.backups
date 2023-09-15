#!/bin/sh
clear
echo "Init build...";
echo " 1/2 ==> Setting new version";

file=`cat addon.xml`
version=${file##*name=\"kodi.backups\" version=\"0.0.};
version=${version%% *};
version=$(printf %.2s "$version");
newVersion=$(($version+1))

sed "s/version=\"0.0.$version\"/version=\"0.0.${newVersion}\"/" addon.xml > addon_temp.xml;

rm addon.xml;
mv addon_temp.xml addon.xml;

echo " 2/2 ==> Commit and push";
#git add .;
#git commit -am "Update to v${newVersion}";
#git push;

echo "

Finish! Update from v$version to v$newVersion";
