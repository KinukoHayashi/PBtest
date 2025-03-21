@echo off
echo "start, bat!"
rem set sendmail=D:\yano\smail-v4.28\nortification.bat



"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_1.dem"  -t 5.66e-7 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_2.dem"  -t 1.27e-5 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_3.dem"  -t 1.27e-6 -E 1 

"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_4.dem"  -t 5.20e-6 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_5.dem"  -t 1.17e-6 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_6.dem"  -t 1.17e-6 -E 1 

"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_7.dem"  -t 5.70e-7 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_8.dem"  -t 1.27e-5 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_9.dem"  -t 5.70e-6 -E 1 

"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_10.dem"  -t 5.20e-7 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_11.dem"  -t 5.20e-6 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_12.dem"  -t 1.17e-5 -E 1 

"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_13.dem"  -t 5.20e-7 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_14.dem"  -t 5.20e-6 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_15.dem"  -t 1.17e-5 -E 1 
"C:\Program Files\Altair\2022\EDEM\bin\edem.exe" -c -i "D:\Guest50um\SAC10_16.dem"  -t 1.17e-5 -E 1 
rem call %sendmail% hayashi 1 test

echo "end, bat!"