teqc.exe -st 2014_01_26_00:00:00 -e 2014_01_27_02:00:00 +obs rec1.14o %3
teqc.exe -st 2014_01_27_02:00:00 -e 2014_01_27_04:00:00 +obs rec2.14o %3
teqc.exe -st 2014_01_27_04:00:00 -e 2014_01_27_23:59:59 +obs rec3.14o %3
teqc.exe -G%~1 +obs rec2_s_%2.14o rec2.14o
teqc.exe rec1.14o rec2_s_%2.14O rec3.14o > mgbh0260_s_%2.14o
del rec1.14o rec2.14o rec2_s_%2.14o rec3.14o