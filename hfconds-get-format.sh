curl -H "Accept: application/xml" -o hfconds.xml "https://www.hamqsl.com/solarxml.php"
echo "band,tod,value,cond_cat" > hfconds.csv
echo "date,sfi,aindex,kindex,xraytotal,sunspot,pflux,eflux,aurora,lat,heliumline,solarwind,magfield,geomagfield,signoise" > space_weather_conds.csv
H1DAY=$(grep 12m-10m hfconds.xml | grep day | grep -o -P '(?<=>).*(?=<)')
H2DAY=$(grep 17m-15m hfconds.xml | grep day | grep -o -P '(?<=>).*(?=<)')
H3DAY=$(grep 30m-20m hfconds.xml | grep day | grep -o -P '(?<=>).*(?=<)')
H4DAY=$(grep 80m-40m hfconds.xml | grep day | grep -o -P '(?<=>).*(?=<)')
H1NIGHT=$(grep 12m-10m hfconds.xml | grep night | grep -o -P '(?<=>).*(?=<)')
H2NIGHT=$(grep 17m-15m hfconds.xml | grep night | grep -o -P '(?<=>).*(?=<)')
H3NIGHT=$(grep 30m-20m hfconds.xml | grep night | grep -o -P '(?<=>).*(?=<)')
H4NIGHT=$(grep 80m-40m hfconds.xml | grep night | grep -o -P '(?<=>).*(?=<)')

DATE=$(grep update hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
SFI=$(grep solarflux hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
AINDEX=$(grep aindex hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
KINDEX=$(grep \<kindex\> hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
XRAYTOTAL=$(grep xray hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
SUNSPOT=$(grep sunspots hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
PFLUX=$(grep protonflux hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
EFLUX=$(grep electonflux hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
AURORA=$(grep \<aurora\> hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
LAT=$(grep latdegree hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
HELIUMLINE=$(grep heliumline hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
SOLARWIND=$(grep solarwind hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
MAGFIELD=$(grep magneticfield hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
GEOMAGFIELD=$(grep geomagfield hfconds.xml |  grep -o -P '(?<=>).*(?=<)')
SIGNOISE=$(grep signalnoise hfconds.xml |  grep -o -P '(?<=>).*(?=<)')



echo "10m - 12m,Day,100.1,$H1DAY" >> hfconds.csv
echo "15m - 17m,Day,100.2,$H2DAY" >> hfconds.csv
echo "20m - 30m,Day,100.3,$H3DAY" >> hfconds.csv
echo "40m - 80m,Day,100.4,$H4DAY" >> hfconds.csv
echo "10m - 12m,Night,100,$H1NIGHT" >> hfconds.csv
echo "15m - 17m,Night,99.9,$H2NIGHT" >> hfconds.csv
echo "20m - 30m,Night,99.8,$H3NIGHT" >> hfconds.csv
echo "40m - 80m,Night,99.7,$H4NIGHT" >> hfconds.csv

echo "$DATE,$SFI,$AINDEX,$KINDEX,$XRAYTOTAL,$SUNSPOT,$PFLUX,$EFLUX,$AURORA,$LAT,$HELIUMLINE,$SOLARWIND,$MAGFIELD,$GEOMAGFIELD,$SIGNOISE" >> space_weather_conds.csv

