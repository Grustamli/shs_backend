# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 09:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0002_auto_20161112_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='body',
            field=models.CharField(blank=True, choices=[('ANY', 'Any'), ('CAR_DERIVED_VAN', 'Car Derived Van'), ('CONVERTIBLE', 'Convertible'), ('COUPE', 'Coupe'), ('ESTATE', 'Estate'), ('HATCHBACK', 'Hatchback'), ('LIGHT4X4', 'Light 4x4'), ('MUSCLE', 'Muscle'), ('MINIBUS', 'Minibus'), ('MOTOR_CARAVAN', 'Motor Caravan'), ('MPV', 'MPV'), ('PANEL_VAN', 'Panel Van'), ('PICKUP', 'Pick Up'), ('SALOON', 'Saloon'), ('SPORTS', 'Sports'), ('WINDOW_VAN', 'Window Van'), ('OTHER', 'Other')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel',
            field=models.CharField(blank=True, choices=[('PETROL', 'Petrol'), ('DIESEL', 'Diesel'), ('GAS', 'Gas'), ('ELECTRIC', 'Electric'), ('GAS_BI_FUEL', 'Gas Bi Fuel'), ('HYBRID_ELECTRIC', 'Hybrid Electric'), ('PETROL/GAS', 'Petrol/Gas'), ('OTHER', 'Other')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(blank='True', choices=[('ANY', 'Any'), ('AC', 'AC'), ('ABARTH', 'Abarth'), ('AIXAM', 'Aixam'), ('ALFA_ROMEO', 'Alfa Romeo'), ('ASTON_MARTIN', 'Aston Martin'), ('AUDI', 'Audi'), ('AUSTIN', 'Austin'), ('BMW', 'BMW'), ('BENTLEY', 'Bentley'), ('BRISTOL', 'Bristol'), ('CADILLAC', 'Cadillac'), ('CATERHAM', 'Caterham'), ('CHEVROLET', 'Chevrolet'), ('CHERRY', 'Cherry'), ('CHRYSLER', 'Chrysler'), ('CITROEN', 'Citroen'), ('CORVETTE', 'Corvette'), ('DS', 'DS'), ('DACIA', 'Dacia'), ('DAEWOO', 'Daewoo'), ('DAIHATSU', 'Daihatsu'), ('DAIMLER', 'Daimler'), ('DODGE', 'Dodge'), ('FERRARI', 'Ferrari'), ('FIAT', 'Fiat'), ('FORD', 'Ford'), ('HONDA', 'Honda'), ('HUMMER', 'Hummer'), ('HYUNDAI', 'Hyundai'), ('INFINITI', 'Infiniti'), ('INVICTA', 'Invicta'), ('ISUZU', 'Isuzu'), ('JAGUAR', 'Jaguar'), ('JEEP', 'Jeep'), ('KTM', 'KTM'), ('KIA', 'KIA'), ('LTI', 'LTI'), ('LADA', 'Lada'), ('LAMBORGHINI', 'Lamborghini'), ('LANCIA', 'Lancia'), ('LAND_ROWER', 'Land Rower'), ('LEXUS', 'Lexus'), ('LOTUS', 'Lotus'), ('MG', 'MG'), ('MG_MOTOR_UK', 'MG Motor UK'), ('MASERATI', 'MASERATI'), ('MAZDA', 'Mazda'), ('MCLAREN', 'Mclaren'), ('MERCEDES_BENZ', 'Mercedes Benz'), ('MICROCAR', 'Microcar'), ('MINI', 'Mini'), ('MITSUBISHI', 'Mitsubishi'), ('MORGAN', 'Morgan'), ('NISSAN', 'Nissan'), ('OPEL', 'Opel'), ('PERODUA', 'Perodua'), ('PEUGEOT', 'Peugeot'), ('PORCHE', 'Porche'), ('PROTON', 'Proton'), ('RELIANT', 'Reliant'), ('RENAULT', 'Renault'), ('ROLLS_ROYCE', 'Rolls-Royce'), ('ROVER', ' Rover'), ('SAAB', 'Saab'), ('SEAT', 'Seat'), ('SKODA', 'Skoda'), ('SMART', 'Smart'), ('SSANGYONG', 'Ssangyong'), ('SUBARU', 'Subaru'), ('SUZUKI', 'Suzuki'), ('TVR', 'TVR'), ('TALBOT', 'Talbot'), ('TATA', 'Tata'), ('TESLA', 'Tesla'), ('TOYOTA', 'Toyota'), ('VAUXHALL', 'Vauxhall'), ('VOLKSWAGEN', 'Volxwagen'), ('VOLVO', 'Volvo'), ('WESTFIELD', 'Westfield'), ('OTHER', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='mileage',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(blank=True, choices=[('AUTOMATIC', 'Automatic'), ('MANUAL', 'Manual'), ('SEMI-AUTO', 'Semi Auto'), ('OTHER', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(blank=True, choices=[(1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], default=2016, null=True),
        ),
    ]
