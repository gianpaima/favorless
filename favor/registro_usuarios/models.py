# Create your models here.
# -*- encoding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
#TipoProgramas:Comedia,Accion,Noticias,Reality,Deportes
class Categoria(models.Model):
	titulo = models.CharField(max_length=60)

	def __unicode__(self):
		return self.titulo

#Ejemplo:Panorama, FA, Yo soy
class Programa(models.Model):
	nombre = models.CharField(max_length=60)
	nombre_abreviado = models.CharField(max_length=6)
	fecha_creacion = models.DateField()
	hora_inicio_programa = models.TimeField()
	hora_fin_programa = models.TimeField()
	canal_programa = models.CharField(max_length=50)
	paises_todos = (('AF','Afganistán'),('AL','Albania'),('DE','Alemania'),('AD','Andorra'),('AO','Angola'),('AI','Anguilla'),('AQ','Antártida'),('AG','Antigua y Barbuda'),('AN','Antillas Holandesas'),('SA','Arabia Saudí'),('DZ','Argelia'),('AR','Argentina'),('AM','Armenia'),('AW','Aruba'),('AU','Australia'),
		('AT','Austria'),('AZ','Azerbaiyán'),('BS','Bahamas'),('BH','Bahrein'),('BD','Bangladesh'),('BB','Barbados'),('BE','Bélgica'),('BZ','Belice'),('BJ','Benin'),('BM','Bermudas'),('BY','Bielorrusia'),('MM','Birmania'),('BO','Bolivia'),('BA','Bosnia y Herzegovina'),('BW','Botswana'),('BR','Brasil'),('BN','Brunei'),
		('BG','Bulgaria'),('BF','Burkina Faso'),('BI','Burundi'),('BT','Bután'),('CV','Cabo Verde'),('KH','Camboya'),('CM','Camerún'),('CA','Canadá'),('TD','Chad'),('CL','Chile'),('CN','China'),('CY','Chipre'),('VA','Ciudad del VaEl Salvadorticano (Santa Sede)'),('CO','Colombia'),('KM','Comores'),('CG','Congo'),('CD','Congo, República Democrática del'),
		('KR','Corea'),('KP','Corea del Norte'),('CI','Costa de Marfíl'),('CR','Costa Rica'),('HR','Croacia (Hrvatska)'),('CU','Cuba'),('DK','Dinamarca'),('DJ','Djibouti'),('DM','Dominica'),('EC','Ecuador'),('EG','Egipto'),('SV','El Salvador'),('AE','Emiratos Árabes Unidos'),('ER','Eritrea'),('SI','Eslovenia'),('ES','España'),('US','Estados Unidos'),
		('EE','Estonia'),('ET','Etiopía'),('FJ','Fiji'),('PH','Filipinas'),('FI','Finlandia'),('FR','Francia'),('GA','Gabón'),('GM','Gambia'),('GE','Georgia'),('GH','Ghana'),('GI','Gibraltar'),('GD','Granada'),('GR','Grecia'),('GL','Groenlandia'),('GP','Guadalupe'),('GU','Guam'),('GT','Guatemala'),
		('GY','Guayana'),('GF','Guayana Francesa'),('GN','Guinea'),('GQ','Guinea Ecuatorial'),('GW','Guinea-Bissau'),('HT','Haití'),('HN','Honduras'),('HU','Hungría'),('IN','India'),('ID','Indonesia'),('IQ','Irak'),('IR','Irán'),('IE','Irlanda'),('BV','Isla Bouvet'),('CX','Isla de Christmas'),('IS','Islandia'),('KY','Islas Caimán'),
		('CK','Islas Cook'),('CC','Islas de Cocos o Keeling'),('FO','Islas Faroe'),('HM','Islas Heard y McDonald'),('FK','Islas Malvinas'),('MP','Islas Marianas del Norte'),('MH','Islas Marshall'),('UM','Islas menores de Estados Unidos'),('PW','Islas Palau'),('SB','Islas Salomón'),('SJ','Islas Svalbard y Jan Mayen'),('TK','Islas Tokelau'),('TC','Islas Turks y Caicos'),('VI','Islas Vírgenes (EEUU)'),('VG','Islas Vírgenes (Reino Unido)'),('WF','Islas Wallis y Futuna'),('IL','Israel'),
		('IT','Italia'),('JM','Jamaica'),('JP','Japón'),('JO','Jordania'),('KZ','Kazajistán'),('KE','Kenia'),('KG','Kirguizistán'),('KI','Kiribati'),('KW','Kuwait'),('LA','Laos'),('LS','Lesotho'),('LV','Letonia'),('LB','Líbano'),('LR','Liberia'),('LY','Libia'),('LI','Liechtenstein'),('LT','Lituania'),
		('LU','Luxemburgo'),('MK','Macedonia, Ex-República Yugoslava de'),('MG','Madagascar'),('MY','Malasia'),('MW','Malawi'),('MV','Maldivas'),('ML','Malí'),('MT','Malta'),('MA','Marruecos'),('MQ','Martinica'),('MU','Mauricio'),('MR','Mauritania'),('YT','Mayotte'),('MX','México'),('FM','Micronesia'),('MD','Moldavia'),('MC','Mónaco'),
		('MN','Mongolia'),('MS','Montserrat'),('MZ','Mozambique'),('NA','Namibia'),('NR','Nauru'),('NP','Nepal'),('NI','Nicaragua'),('NE','Níger'),('NG','Nigeria'),('NU','Niue'),('NF','Norfolk'),('NO','Noruega'),('NC','Nueva Caledonia'),('NZ','Nueva Zelanda'),('OM','Omán'),('NL','Países Bajos'),('PA','Panamá'),
		('PG','Papúa Nueva Guinea'),('PK','Paquistán'),('PY','Paraguay'),('PE','Perú'),('PN','Pitcairn'),('PF','Polinesia Francesa'),('PL','Polonia'),('PT','Portugal'),('PR','Puerto Rico'),('QA','Qatar'),('UK','Reino Unido'),('CF','República Centroafricana'),('CZ','República Checa'),('ZA','República de Sudáfrica'),('DO','República Dominicana'),('SK','República Eslovaca'),('RE','Reunión'),
		('RW','Ruanda'),('RO','Rumania'),('RU','Rusia'),('EH','Sahara Occidental'),('KN','Saint Kitts y Nevis'),('WS','Samoa'),('AS','Samoa Americana'),('SM','San Marino'),('VC','San Vicente y Granadinas'),('SH','Santa Helena'),('LC','Santa Lucía'),('ST','Santo Tomé y Príncipe'),('SN','Senegal'),('SC','Seychelles'),('SL','Sierra Leona'),('SG','Singapur'),('SY','Siria'),
		('SO','Somalia'),('LK','Sri Lanka'),('PM','St Pierre y Miquelon'),('SZ','Suazilandia'),('SD','Sudán'),('SE','Suecia'),('CH','Suiza'),('SR','Surinam'),('TH','Tailandia'),('TW','Taiwán'),('TZ','Tanzania'),('TJ','Tayikistán'),('TF','Territorios franceses del Sur'),('TP','Timor Oriental'),('TG','Togo'),('TO','Tonga'),('TT','Trinidad y Tobago'),
		('TN','Túnez'),('TM','Turkmenistán'),('TR','Turquía'),('TV','Tuvalu'),('UA','Ucrania'),('UG','Uganda'),('UY','Uruguay'),('UZ','Uzbekistán'),('VU','Vanuatu'),('VE','Venezuela'),('VN','Vietnam'),('YE','Yemen'),('YU','Yugoslavia'),('ZM','Zambia'),('ZW','Zimbabue'),)
	paises = models.CharField(max_length=2,choices=paises_todos,default="PE")

	dia_programa_todos = (('LV', 'Lunes a Viernes'), ('SD', 'Sabados o Domingos'),('NA', 'No tiene'),)
	dia_programa = models.CharField(max_length=2,choices=dia_programa_todos,default="LV")
	#Estado:Disponible,Cancelado,Break
	estados_todos = (('Di', 'Disponible'), ('Br', 'Break'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Di')
	logo = models.ImageField(upload_to='fotos/',blank=True,null=True)
	descripcion = models.CharField(max_length=200)
	#LLave Foranea Tipo_Programa
	tipo_programa=models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.nombre
		


#Preferencias-> Gustos de los usuarios por los programas....
class Preferencia(models.Model):
    slug = models.CharField(default = 'le gusta', verbose_name='PreferenciaSlug', max_length=100, help_text='Denota el gusto o preferencia del usuario')
    fecha = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Usuario', related_name='Preferencia')
    estado = models.BooleanField(default = True)
    programa = models.ForeignKey(Programa, verbose_name='Programa')

    def __unicode__(self):
        return "  %s , %s"%(self.user ,self.programa)

#Integrantes de los programas
class Integrante(models.Model):
	nombres = models.CharField(max_length=60)
	apellido_paterno = models.CharField(max_length=60)
	apellido_materno = models.CharField(max_length=60)
	foto_a = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_b = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_c = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_d = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_e = models.ImageField(upload_to='fotos/',blank=True,null=True)
	programa = models.ForeignKey(Programa)
	

User.add_to_class('foto', models.ImageField(upload_to='fotos/',blank=True,null=True,default="fotos/default.png"))
User.add_to_class('nombreCompleto', models.CharField(max_length=20))
