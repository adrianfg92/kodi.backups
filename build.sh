replace="1";
LINE="<addon id=\"kodi.backups\" name=\"kodi.backups\" version=\"0.0.5\" provider-name=\"adrian\">"

echo $LINE | sed -e "s/2/${replace}/g"
#echo $LINE;

exit;
