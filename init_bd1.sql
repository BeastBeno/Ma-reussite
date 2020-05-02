DROP database IF EXISTS bd_universitaire;
CREATE DATABASE bd_universitaire;
USE bd_universitaire;

CREATE TABLE Programme(
	sigleProgramme varchar(100) PRIMARY KEY,
    nom varchar(100),
	credit smallint
	);

CREATE TABLE Etudiant(
	idul varchar(100) PRIMARY KEY,
	nom varchar(100),
	motDePasse varchar(200),
	motivation smallint,
	credit smallint,
	sigleProgramme varchar(100) NOT NULL,
	FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE
	);

CREATE TABLE Service(
	id smallint PRIMARY KEY,
	nom varchar(100),
    disponible smallint(1),
    sigleProgramme varchar(100) NOT NULL,
    FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE
	);
    
CREATE TABLE Directeur(
	mail varchar(40) ,
	nom varchar(40),
	numeroTelephone varchar(100),
    sigleProgramme varchar(100),
    PRIMARY KEY(mail, sigleProgramme),
    FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE #Modelisation de la relation possede un directeur
	);
    
CREATE TABLE Objectif(
    idul varchar(100),
	id smallint AUTO_INCREMENT,
	sessions varchar(100),
	nom char(40),
	concentration varchar(100),
	moyenneSession smallint,
    moyenneFinProgramme smallint,
    moyenneCours smallint,
    sigleProgramme varchar(100) NOT NULL,
    PRIMARY KEY(id), 
    FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE, #modelisation de la relation posseder
    FOREIGN KEY(idul) REFERENCES Etudiant(idul) ON DELETE CASCADE #Modélisation de la relation posseder
                                                                   # Ca va permettre davoir un lien entre etudiant et objectifs
	);

CREATE TABLE Cours(
	sigleCours varchar(100) PRIMARY KEY,
	nom varchar(100),
	credit smallint,
    evaluation smallint
	);

CREATE TABLE Suivre(
	idul varchar(100),
    sigleCours varchar(100),
    sessions varchar(100),
	moyenne smallint,
    PRIMARY KEY(idul,  sigleCours),
    FOREIGN KEY(idul) REFERENCES Etudiant(idul),
    FOREIGN KEY(sigleCours) REFERENCES Cours(sigleCours)
	);

CREATE TABLE Concentration(
	id smallint PRIMARY KEY,
	nom varchar(100),
	sigleProgramme varchar(100) NOT NULL,
	FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE
	);

CREATE TABLE Appartient(
	id smallint PRIMARY KEY,
	sigleProgramme varchar(100),
	sigleCours varchar(200),
	typeCours varchar(1),
	disponibilite varchar(3),
	regle varchar(1),
	creditRegle varchar(1),
	FOREIGN KEY(sigleProgramme) REFERENCES Programme(sigleProgramme) ON DELETE CASCADE,
	FOREIGN KEY(sigleCours) REFERENCES Cours(sigleCours) ON DELETE CASCADE
	);
INSERT INTO Programme(sigleProgramme, nom, credit)
	VALUE
	('GMC','Génie mécanique' , 120),
    ('GCI','Génie civil' , 120),
    ('GEX','Génie des eaux' , 120),
    ('ENV','Environnement' , 120),
    ('GCH','Génie chimique' , 120),
    ('GIN','Génie industriel' , 120),
    ('GEL','Génie électrique' , 120),
    ('GLO','Génie logiciel' , 120),
    ('GGL','Génie géologique' , 120),
    ('GMN','Génie des mines et de la minéralurgie' , 120),
    ('GIF','Génie informatique' , 120),
    ('GPH','Génie physique' , 120);

INSERT INTO Etudiant(idul, nom, motDePasse, motivation, credit, sigleProgramme)
	VALUE
	('DIBAX', 'Diete Baxter', 'c6b46dc21387f8c4a4c3cd1eab631b8e94494244b84203bb1e9003852163b692', 7, 66, 'GIF'),
    ('GAJAC', 'Gart Jack', '9de0c2e512f5786b963ae6620c68968b2481ee71f5861edf450678828a08a671', 3, 57, 'GIN'),
    ('DUFEL', 'Dunca Felix', 'd569113e84131e67b5c1c08aea81b138dceed8cf9e2e665f299b216ed3d9752e', 0, 77, 'GIN'),
    ('MASTE', 'Malcol Stewart', '9f04722331147761c57ca9cfdeca2d12638665e86257748a7742758709225d31', 1, 23, 'GMC'),
    ('PRISA', 'Prescot Isaiah', 'a0534928882c80c0847f8a312e4b41162400ea194d12fdc6746513d41246347b', 5, 78, 'ENV'),
    ('KIHOL', 'Kir Holmes', '4ca8c0d49644727fc381aea61e539d25aa2125d410282b7a9ecc63ae549e2180', 1, 20, 'GGL'),
    ('QUSET', 'Quama Seth', '240e6fec27d1917eca31201a156745f1933ad7aa00707b8fc5e22a00fa554538', 9, 87, 'GLO'),
    ('GAGRA', 'Garriso Grady', '81a35d403d870df935cb8df2b906f7ae3161eb0f17a5449ecff7cb13e37641ab', 7, 49, 'GEL'),
    ('DOBEA', 'Dola Beau', '1ad9a2daeea98721987e5e45ae15699e2b52f55a8fb1b07a533d6bc7b2b984fb', 2, 89, 'GPH'),
    ('WYHEC', 'Wyli Hector', 'd95813942689c630322d3acb8cccf2263b614a76dd6a24d963204917c2c056ab', 4, 100, 'GIN'),
    ('THSTE', 'Tho Steven', '1e8ac13c315fea22ff85c3bd8d6cda904529827326ce976773d2e12be2de18dc', 6, 98, 'GIF'),
    ('FENOA', 'Ferri Noah', '523bcb95c9de1e5ed74e1966863e008e428a9d19662ef0b79ccf53ded88f0db6', 3, 114, 'GGL'),
    ('HAIGN', 'Hamis Ignatius', '1f2c769f164c5ef5491fb4dff65e41804441b1a29330c6db1ad093cc561db4c8', 6, 111, 'GIF'),
    ('ORCOL', 'Orland Colby', 'a83870643c41d05f2076d76d35851c73539634a805db669428197d902fa6c103', 7, 82, 'GCH'),
    ('LEJAM', 'Lewi Jameson', '1b5b2c38e27187f47ddf8aeab0bb6ed0f8d1e17c4766a9099c7f9c592f935cb5', 8, 55, 'GCI'),
    ('VAMUF', 'Vaugha Mufutau', '351a686432cf03f419d248c46cf305ae14c0a1165bd99cba1e65d797fac0b4d5', 9, 71, 'GMN'),
    ('JOART', 'Josia Arthur', '0696d4a3cc6c8509ce5d28ee7b44abd0208ef257568c5f1f18269b95d14d2e6c', 6, 16, 'GPH'),
    ('ALWAN', 'Allistai Wang', '503bcd08ac2bbf331f515c24f6d4dd46fef70d44e0d178b05ca8fae35a0d7851', 7, 65, 'ENV'),
    ('GAPRE', 'Garret Prescott', '151a2cfb23f52b88f8dcdedc5e9f652d07b7e8e4558c15c9ea40dc17c0c9a734', 6, 74, 'GIN'),
    ('GAREE', 'Galvi Reed', 'd98ff53a8fb952d821c63f0543dc17d2edee13f4890c5aeb089d613b15734b38', 1, 82, 'GEX'),
    ('DEPRE', 'Devi Preston', 'd650b096a9575ecc9593aaade24dac9373e1d748ba01d57ba2938da77e090b16', 9, 20, 'GEX'),
    ('SHGAR', 'Sha Gary', '3586039f1b360ef3e2b192e0d021d1d11358a876ee323bcb52311dc423ece744', 3, 97, 'GEX'),
    ('HAEMM', 'Harla Emmanuel', '2de190befd8c58c9e0433d01492980b3b8ae63b7ecb381b1c39e6276d8ad37b5', 4, 93, 'GEX'),
    ('LEIVA', 'Le Ivan', 'ea4b648ccd2398aa1088a0da277ca21ab13cdc03f0914bcdf62c42024e74498b', 1, 51, 'GIF'),
    ('SOBER', 'Solomo Bert', '7456c5f8a67f3909ae584b9d4c30725869520d521b901f9b746e4c8e5aa1d6e8', 3, 79, 'GIF'),
    ('EAURI', 'Eaga Uriel', '7f14550af6c1b67c9d39f27acb27c1bfb7a95bf4b1a444ed55546cce9be5fd6e', 5, 26, 'GMN'),
    ('ROGAN', 'Rona Gannon', 'fefa74b150133e3b30f00c8e3cfc8f8734f4b2f0d7fa9f57630d18c3e1d2bd8d', 0, 4, 'GMC'),
    ('JEKEN', 'Jermain Kenyon', '8ea6777ab7aec6adc246bc57a88c088d30762e85ac4608a6b934ddd593f10946', 3, 117, 'GMN'),
    ('TIALF', 'Timoth Alfonso', '9cfc5a8599b8705254b7d6ba40acde7e367a7f5adce1b2d31a8adce61f600103', 9, 26, 'GIN'),
    ('HAGAL', 'Hal Galvin', '6180a726a51140607f062eee721b997e86b372fd9fe003ba5cb5e97ce70a3912', 7, 11, 'GIF'),
    ('MAWAN', 'Marshal Wang', 'd3191a5239d007c08345f5ae6a9021d1ad9f9f8eda3c6aced656727eb9075beb', 0, 107, 'GIN'),
    ('WALIO', 'Walte Lionel', 'd1e2d33910ed6ccdafb72bddf78b815ad574465584ec765011951df7273f2d5c', 8, 54, 'ENV'),
    ('JUDOR', 'Julia Dorian', '197b878a24e2b69c66a1e0380128a1b7ca929c568b2a3e86d5c6ab195889429e', 3, 90, 'GCI'),
    ('RYDIE', 'Rya Dieter', '8dfcbb1a180b23b5e01d6b4ff4f460f8c6f1703b5fd09d4d289c69282cf424da', 9, 56, 'GLO'),
    ('ISGUY', 'Isaia Guy', '8b4b20d9ae64ccd93aa43480db88e4af0636f7ca782cb820ab78015e8bd32068', 5, 76, 'GCH'),
    ('FIJAC', 'Fin Jack', 'c8bf15e942e130329e944f510beb7b07fc24cc605943e808a91cce41cb2581d1', 7, 83, 'GGL'),
    ('BRJOS', 'Brenda Josiah', '43137d3fcd15ee06fc930d67ac711b04411afd6890e26ea5b7a42f2536340e70', 2, 97, 'GMN'),
    ('VIBLA', 'Vincen Blake', '85fb80ac8a2a8fc3d36b0d47f411a07ec9a70e816cb536aa81831c56d4c4c664', 6, 4, 'GLO'),
    ('EMTRE', 'Emmanue Trevor', 'eaf82d7790902e284be9dab95269b7da7b4fa374de49b2c11965df1aa8856b8f', 5, 48, 'GCH'),
    ('JOCOL', 'Jona Colin', '812ed678e65c46d3c720b596b0a564b4d4ad988bdcf33ef96019df15d7caa2f6', 2, 7, 'GMN'),
    ('BRCOL', 'Brende Colton', '5e38828f6a4e0d37ac74cfdb2f9c87891e97aa8d70e7d3abbc3ec9a3f707eab1', 6, 13, 'GEL'),
    ('HAHAM', 'Harriso Hamilton', '8d4f9aeb1b31763bbae12fc72247b89c0001d6b84844878d99c24609313dc293', 3, 68, 'GMC'),
    ('DABRA', 'Dal Brandon', '5036183589a9c94f3869b485af45222b077d43c0292e01256bafeb82e337cccb', 7, 79, 'GEL'),
    ('QUJAR', 'Quenti Jarrod', '79bd5776a2f045a4c83de5776273662a373a405529083b6d0a30d0fbd97193e5', 3, 78, 'GCI'),
    ('KYJER', 'Kyl Jerome', '3e4ece053548996c4b4ccf43111b552192af26acbf25abb42a9c433e2248b8a7', 5, 79, 'GMN'),
    ('STGEO', 'Stee George', '10750d6e86cd9e1d07304fce8636e3916df50837f7aa18218e9a160d84e950f8', 8, 41, 'GEX'),
    ('COJUL', 'Coope Julian', 'f191641376952e9655092092aaae43cd7b44493322be4f2cd733819443dfcaee', 5, 59, 'GGL'),
    ('KICRU', 'Kiera Cruz', '4f1797008f69f2fc98a876472106246e2703c0bd989b393f13e6e67c9e814ada', 4, 117, 'GIF'),
    ('TOGRA', 'Tod Gray', '4e985ff1a0f42d9a6444bf683c6168e023a6d8e437ee44df4fb506f8274c48f3', 2, 93, 'GMN'),
    ('SAFUL', 'Sawye Fuller', '1b604b9a4eebaab76000a071108ec1dd6facb99390d5f58e5176f34fa53f9569', 8, 39, 'GMC'),
    ('JECHA', 'Jelan Charles', '0cac21277548197c42a4e29bb0e16c387880d6869b4b5543591fc711f11f983c', 0, 114, 'GPH'),
    ('THNEI', 'Tho Neil', '48ae86ab3a55607893ea364daf101216281deef2819fd76cf6cc36f1ff371ba7', 9, 17, 'GEX'),
    ('JACON', 'Jaspe Conan', 'e5ced4f44b3999989e2079a5ebb94014bd9f6c63813029bd4fa77ebce46e0709', 8, 33, 'GCI'),
    ('JOTOB', 'Jona Tobias', '251830ce5b39b7261d06baabd40781234e75aeaf4d428fa14564d29c1e8e6056', 0, 22, 'GIF'),
    ('BATHA', 'Bake Thane', 'b394eeb92a59ecd82bedae693e4811bc62d86ed9d282d11465f91d9faae88664', 2, 48, 'GIF'),
    ('DOBRU', 'Domini Bruce', '079e106bb621ffb908de07d5e12f9c86455a1fb2fc249c3c5df68976bd10ae8f', 4, 11, 'GLO'),
    ('RYLAM', 'Rya Lamar', 'f621834b0649dbf99a8dd7f2d98cbff63ef3e9b9fb6151ab17033d529eb62c13', 8, 36, 'GMN'),
    ('BRBUC', 'Bren Buckminster', '3f23160f7670b95b10ad41dbced9aa5c6c1d436e20583a3a88ee96b297697c6b', 7, 45, 'GEX'),
    ('BEZAH', 'Bec Zahir', '021e9c8096655663ed4790f51736e1ae9dfbcebdafb98475ac750a6c512a337a', 8, 77, 'ENV'),
    ('CHCOL', 'Chadwic Colby', 'f6c3b88ccb76e86fac37f7b2df527fefc4a3bd468c4d02792d7d3ed69efcc003', 2, 115, 'GEL'),
    ('MUROS', 'Murph Ross', '9e6b9010a1d1bfade8a1fdc82243f91cb07457f828f8caf70c84336533e7d5a3', 7, 7, 'GPH'),
    ('MUXAN', 'Mufuta Xanthus', '068ce753fa21a203c72e7f82c66106ce9f22b80c0cb1db77dfcb596fab1c5334', 8, 73, 'GCH'),
    ('HALAW', 'Hashi Lawrence', '5d7d6068b8d04d3e28c1606927cbd050415d7266bbd6cc5eb8c57084db15a7a6', 6, 48, 'GIF'),
    ('OLLAI', 'Ole Laith', '80d9610da13eab6718ed1186f2c3927765c900913afa642e77eb37e8e109b739', 6, 18, 'GIN'),
    ('LEALE', 'Le Alexander', '66a4c9bdda4ad7846c53771ec19ccef8e03bc527c2dc64f9a26c18cce663090b', 5, 93, 'GIN'),
    ('JAMAR', 'Jare Marvin', '3eea22e8acce5915bbad2297a67ccc3327b3806fc4a576a4f3c8339063dac2d8', 9, 95, 'GEL'),
    ('HYFEL', 'Hyat Felix', '5375ec3e310dd4f467864e37710406e886c69e06ed7d657c88c5aca950521b98', 5, 60, 'GMN'),
    ('GECAL', 'Georg Caldwell', '718ba10ebff2bfec50c5c8640d1dccc52fb9d1d17fab77f4c9acadf4d667c176', 5, 115, 'GMN'),
    ('HAMUF', 'Hamilto Mufutau', '62e9aba35b6e172401ac2e19b9b70e0b65c44a1e9d4b6943a6404eaad81858ac', 3, 49, 'GEL'),
    ('BRNEI', 'Bren Neil', '83435998b3e83f57e58ca5d72a0c3d0d2efaf5e891131da3c299a8d4000f0084', 1, 115, 'GCH'),
    ('ZEJOH', 'Zephani John', 'e66dec59d99f2fd60a12c50af6a3af9b6e1b23eaf9cdb42f94a1894241de3bb6', 5, 11, 'GMC'),
    ('LUAME', 'Luk Amery', '13b53c4864ed7aebe8e70169fd5ff3b260a5bc514d25bb73e6c4b2ef3b7910d1', 8, 42, 'GGL'),
    ('HEPAU', 'Hedle Paul', 'a85109b79e52898f3d861d95e39fe399c538acf1a4799623621b5e21cb411cf9', 2, 78, 'ENV'),
    ('ARSET', 'Arseni Seth', 'cee4f00efe4cc634e32bc638b96d1e8e9f9d0363cd5c6dc8a59cd3c9473b55b1', 5, 98, 'GGL'),
    ('HAJOE', 'Harpe Joel', 'd21ec2c1e859ea970b65dded0a615334b61a32fba3473ccb0270c9c533bee53f', 3, 37, 'GCH'),
    ('GADEA', 'Garet Deacon', '8fbb8639d32d5fa4bd7df712e0371e5f1c04e3f3a8ffef2d0fd05710387bae61', 0, 42, 'GMN'),
    ('FLBAR', 'Fletche Barclay', '07d7a0ed7cfea4fc8daddbd8f769d038f928fb56ef0b976b8223b9e56d07a37f', 9, 79, 'ENV'),
    ('BRJEL', 'Brande Jelani', 'a36fb06d1f7cae40600c01606bd9bf11674e457f8134a6cb974fd5c166cce7f6', 8, 16, 'GGL'),
    ('XEHAR', 'Xeno Harrison', 'b8b61be2616713ab2a6f33a6deae728f2a1df497968973a9a3d23aef140b1070', 7, 25, 'GEL'),
    ('EVCHA', 'Eva Channing', '5acc08714de09a015e8387cba7fbd1d28e195c5c30c37fe273ccb13c32a8f6b4', 2, 0, 'GIF'),
    ('FRHAL', 'Frit Hall', 'cbc9c184b435f32c8e3b2500385638028d67a867da9b3ac6673ff5d1917f5f94', 7, 52, 'GMC'),
    ('MAGAR', 'Maco Garth', '5833106f70b8852b88a00d07b0e4db19a61ce6e44b0a5274afb9423959adc503', 4, 105, 'GPH'),
    ('RODIE', 'Roga Dieter', 'dbe31892563ed001943c8be8342dcd2f2b8e6f0653dbfb2c1128f93969f4cae0', 4, 13, 'GIF'),
    ('ARISA', 'Arseni Isaac', '49d66a367ebc4ffbe1556f62bdb419f2ffd4c5ac35ae1b097659e8d749937397', 3, 45, 'GEL'),
    ('JOHUN', 'Joshu Hunter', '86e307e1bb15d6710b61acd778f0aa5d23b21a79f7ca2f2f48e21b9ef335df96', 2, 18, 'GCI'),
    ('QUJUD', 'Quin Judah', '16f63587a44625a45dc4a3458b27f019e8789ab525367fdf6c16ad10a1eb7065', 6, 53, 'GGL'),
    ('HOGAB', 'Honorat Gabriel', '547857a94e741c91b44147425ecf99ecbed608f9b6d2ccda4ba637b61ee5e74d', 0, 27, 'GIF'),
    ('FUHAR', 'Fulle Harding', 'e5f0ef3a2a8699089d792c8e4f88c76474ba30ce09a7b485ff167bcf1c079ab8', 7, 119, 'GIN'),
    ('ANCHE', 'Andre Chester', '181c25f76aac4b3b883151f289ded2517b6518f9a49ae22f22e7caaa9c6c9e79', 9, 39, 'GCH'),
    ('CHKEN', 'Cheste Kennan', '2b3b1abb24e2a96ea25f90f9235db08dc3deeed490bb4f247b144a3350788332', 1, 82, 'GEX'),
    ('BALAN', 'Barr Lance', 'e3c8340fa5a0364d1d9bf9b7063dc12f1132d8314a4565fcc30e7b76a8898489', 7, 110, 'GGL'),
    ('DACUR', 'Dariu Curran', '85f61b38398ec300fef5bf3a122a094f2da7dd746d9ceb0b6340bf68841f7367', 9, 108, 'GEX'),
    ('NIWYL', 'Nissi Wylie', '613b00e72513a3404a460a7cbcbd44d4356d692e7556720eced238acc490584f', 4, 102, 'GPH'),
    ('BRMEL', 'Bria Melvin', '9f2f4b525c043d678fbc70165db80f95df9b3c8d907d34e8d8c25f1f3cbc9660', 5, 34, 'GCH'),
    ('JEGRA', 'Jerom Grant', 'f2ed9729a4db1e0bca5a43dad1d68196a21a07b5076135769344a7c675e39acf', 3, 14, 'GCH'),
    ('BRLUC', 'Bria Lucas', 'b332f5a1c0676082ed3bce376c90872fc870ef01f07d7e2aff12c335c312b4ab', 7, 20, 'GEX'),
    ('ELCHA', 'Elvi Chadwick', '4cffef44dfe9ed73264609d79630558de73d5e49d369aef6555937d67eee7bfc', 7, 94, 'GCH'),
    ('CAKIE', 'Caesa Kieran', '7a0457a73d00eb2648c176d16021f89bd74200e90b489997a5487677fd527edb', 1, 24, 'GMC'),
    ('PEWAD', 'Perr Wade', 'd58da725e8e716f57a84a730e0bb9cf4156a43598d122ee50c62e4d066d25400', 7, 21, 'GGL'),
    ('SOMAG', 'Solomo Magee', '50c0f1581fd8943f31145155258e7e54a6377ba314e1213f4e0e70effa65e8ce', 7, 8, 'GEX'),
    ('CHISA', 'Chantal Isabelle', 'bbac729b287f6277ddfd7efbe218cc9e8908412097bf9b9e338074b6e067c0ce', 8, 90, 'GMN'),
    ('KIZOR', 'Kitr Zorita', '3f5ff49408253bd7c8d8c8e4c927d2766e7ee9d32e6f9812d1049afa5c0322fc', 2, 97, 'GLO'),
    ('MEJOR', 'Mega Jorden', 'a2ad0cd2d010896e81c1c272fd7bd7393d1434092bf42536b892b0b16202653b', 1, 46, 'GEL'),
    ('MAMON', 'Maria Montana', 'c1602fa492ecf657bb0096bd719e23bc4a573def19a35db5f66de786764066a7', 3, 101, 'GGL'),
    ('ALMIC', 'Alin Michelle', 'a1c78b60c29437f0cbe27d15971fae418724ab2c2720231ac40d4b58f4183569', 9, 38, 'GGL'),
    ('ROMER', 'Rosaly Meredith', 'e5b3e5d8059c9dc93439f378e7ce1a6e9a8d47e08e781fdc88efe89acbab7382', 2, 119, 'GLO'),
    ('DOEMM', 'Doroth Emma', 'c5b50ef259fe6b03ba75865ab0d8ee46326a981b2a39534cd1e45c040f8efe48', 3, 89, 'GCI'),
    ('MAHED', 'Mar Hedda', '505aba4258b26e1eaf0b26d64646290a7c5edb85421957c309350cda0282e3c3', 4, 82, 'GCH'),
    ('PHGIS', 'Phoeb Giselle', 'c0e6e9f7e6c8e5779862365f67857c4aba5fb851be3e58e0a7668b2d73f701c9', 0, 11, 'GPH'),
    ('CAIDO', 'Calist Idona', 'f3fcb1e7f14633a427cde3b9ddc4c94ceebfe8df4f22fb3362d82b49727c3861', 1, 106, 'GPH'),
    ('TAJES', 'Taylo Jessica', 'b18746e3f6d10c1735bf34ea449e05052f52bf49cad6a45e72fe2ce7bea7a5b6', 2, 6, 'GMC'),
    ('EVKYL', 'Evangelin Kylie', 'd2d894d57995b1a09ce44c38328a4669c41836c98eafc263e35b9bdcded7240f', 8, 84, 'GCH'),
    ('HEHER', 'Hele Hermione', '08b9c1b0fadc91dbe34679dfc44418fe4cd43a556b2d86715fbe3c43f1c9709f', 0, 86, 'GEL'),
    ('DIAME', 'Dian Amela', 'c1066f5830872ed294d3ae7bb832ead6eb0c4b8514649cfac93bdb01732bacfb', 1, 28, 'GGL'),
    ('COSAC', 'Collee Sacha', '4b575a9a78b5faabc4e344529badb5ce555c227a319de8d1a741a6f35e932bfd', 4, 102, 'GCI'),
    ('KELAU', 'Kessi Laurel', 'bd0627f2b682d587888fe81549a457903f99f7b77850f6938f794fe924fc69d5', 9, 28, 'GMC'),
    ('WHCLA', 'Whitne Claudia', 'c1f8de6a510143ea71c3d273527ffcfc3bad771a1fc016ed172e5e058a68262f', 2, 18, 'GIN'),
    ('HECHA', 'Heathe Chantale', 'aaba4aac3f6f97b710d5fa0a08272931df87efc319f1c36158b6c9fb1a5d48cd', 3, 58, 'GEX'),
    ('KRCHA', 'Kriste Chantale', '6b17b499ea4c9ac7e652864ad9ac790fbf4f1141db0d9e1fd2257dadced3818d', 1, 57, 'GGL'),
    ('DANEL', 'Dakot Nell', '2c17a147fc00056d702aacb23ed0a34e4837c611f189edc718da0c2a86fa257b', 2, 104, 'GIF'),
    ('JOKYL', 'Joell Kyla', '81afc8a352eefcfecbca0b84abd92e76fec48ed3602a00b3a06badb859e759b5', 9, 118, 'GCI'),
    ('WHJAD', 'Whilemin Jade', '5225e0a97c59bb0c77567ebf69161cb37b4636a2de5d66da4a6819766d6c6bba', 8, 30, 'GCH'),
    ('ALLEA', 'Alis Leah', '537e415b040b457e25299fe59fe983bd685a85bea8660049410dea5b286c3012', 9, 97, 'GEL'),
    ('SYBLA', 'Sydne Blaine', '3a9b14e4dd519bd97601e6d91a32d38f00cb2ce8608432906b3b7a948b78bb6a', 1, 107, 'GGL'),
    ('RECEL', 'Rebeka Celeste', '516b53a8a96cb4226856d9905d17a06b8a79d13432d984b1ea27b06107527a8e', 3, 72, 'GEL'),
    ('SHRIS', 'Shaeleig Risa', 'bd9b5f54f0721c183eb54d77f8de1165411a7eb1b143e35b91d4b80fe25a7722', 1, 102, 'GIF'),
    ('SOLIB', 'Sony Libby', '17f87957ebb53b4bca7b445bc873af443d470ce3eb49af90d4ade7676f7d49b8', 2, 71, 'GLO'),
    ('KYCAS', 'Kyle Cassady', 'f16f65dabd6ad3c22db79c3a689f5144c062eeeb8788c8dc0ff564592a15cc71', 7, 103, 'GIN'),
    ('AYLIL', 'Ayann Lilah', '5bf0619c83fcd04eec1e44d0f767aafe76c3c53cbbb83d0d11db6f4ea8c38a1d', 7, 33, 'GIF'),
    ('SYMAL', 'Sylvi Mallory', '429878151bef8552e57ac2a946203eb04c44600d1926f84cfab41cf014a3f516', 0, 69, 'GPH'),
    ('MOJAE', 'Molli Jael', '12a0cd5cf9fecce8a3f9d788e9bb9a77375dad99c4177e4210170e201ba45913', 4, 117, 'GIN'),
    ('KIEME', 'Kimberl Emerald', '5d55bc4828039607ae324d8ade96572d3c9420831d1669164ce51318d9aefcf6', 5, 23, 'GCI'),
    ('NOQUY', 'Noell Quyn', 'af77fd0abb5aa59bd1aaa360c3767740693a38f21c11263b18cf1eccd4fa9169', 2, 23, 'GMN'),
    ('LYOLI', 'Lydi Olivia', '550a9fc13590e73c903d141948be8016d649eece10016d56f71f892c5f06be28', 2, 104, 'GCI'),
    ('APMAD', 'Apri Madeline', 'da45325019933672bfc859d7cfee16029627ec0cb1b2052fc666f9067e5f3844', 6, 68, 'GEX'),
    ('JAIRE', 'Jad Irene', '662890f5ef504135d599d09ffb7f4129bbc9b0c186dddb3c60e3db8708e50b1a', 6, 107, 'GIN'),
    ('KIPOR', 'Kirste Portia', '7bab9ca21cdf6e69048e37e8bf22f4b3f1c003c2d90339932e30c04db851137f', 6, 38, 'GCH'),
    ('IMMEL', 'Imeld Melanie', 'e534692ae3a6b0c7f45b78960af5f7df985d386867a368b906fb60e9800c28ed', 9, 109, 'GMC'),
    ('MILIL', 'Mirand Lilah', '8fbf2f8402124c3b811294773afb74784d2623ddade6188dd2a2cb30195c5815', 0, 70, 'GCI'),
    ('BETAS', 'Bell TaShya', '866355d259fc587e2cc697cde8efe53d2f06e65d0b5a084a83e34154c1332dab', 1, 103, 'GCH'),
    ('JOGAI', 'Josephin Gail', '7366bea09bc0d17bf43883f70d1b5bd296364181a30bd0ccbdd4124094fc682c', 1, 98, 'GCH'),
    ('URDAR', 'Ursul Daria', '1733cf2cb5d0d43bc43ee8919e405897605e2babb6e755c490767043d4e1f3d9', 7, 15, 'GGL'),
    ('TEQUI', 'Teega Quintessa', '51229fd2bb71eda512a63f834b624b41b8bbd40c16726f742cbcbfef1cedc88f', 0, 46, 'GEX'),
    ('CIMAR', 'Ciar Mara', 'a557d801ee3ce08bdc8006c2f76a51ce661d40d070f99949d20e9c7689d4b295', 8, 98, 'GIN'),
    ('BAJOA', 'Barbar Joan', '81742ecadf3179561a8f7b4c285da4266952f2d63cbf847012a861774a4da67f', 4, 36, 'GMN'),
    ('GRSAN', 'Gretche Sandra', '181a32b7afd595e5ca64bbe051b83f670b15cb324dddeca63e484eaf9872e7cc', 9, 48, 'GLO'),
    ('KYARI', 'Kyle Ariel', '3d557a0014b92031dfad78527bf276169b4575860352ffac5bafa9eba011b65d', 1, 68, 'GMC'),
    ('COMAL', 'Constanc Mallory', 'b0ab2c72ad28447782617492eaf6f7fb83f9a63d5ce319be2b99c561ec3aa1b8', 7, 39, 'ENV'),
    ('MANAD', 'Mara Nadine', '9c4e806322417b69d8f97337b64b808167d1d9988e88b33b1b3b0e9d9de6bfda', 7, 71, 'GIF'),
    ('SHELA', 'Shelli Elaine', 'ae0bb40c4af198e49e99c47826117becf6c08a1d767b8f3fbc2a653e2db52736', 7, 31, 'GIN'),
    ('ROGAY', 'Ros Gay', 'c05c20a3059047afdcee4245e46b4b16af2be965402cee01e72d91de114b74cc', 5, 110, 'GMN'),
    ('ALJES', 'Alexandr Jessamine', '302349f14cdc928744aa6bfc579e473c20accacee09e1506e12112d66d0169aa', 0, 16, 'GEL'),
    ('BRYET', 'Britanne Yetta', '9ff635d6b0dff3853568b7cb7bf9f192f621dbbbcaabead66cc6929db2cf1588', 5, 103, 'ENV'),
    ('SHJAC', 'Sha Jacqueline', '1fd28ccf48ea69000fa3dbe4655b463f95c112b3b85d6aa6e3efad46c9daec51', 4, 119, 'GEL'),
    ('HAKEV', 'Hayle Kevyn', '2256b128436bd5d4484623853dd8d077dc6bf00029d6d362d240a3733f9ad89a', 1, 71, 'GCI'),
    ('BAMAR', 'Basi Mariam', '50602e32c93807fe998600e1a35cd13ffaebf3ea9d86ff018bf04c4789ee3882', 8, 101, 'GCH'),
    ('SALIL', 'Sach Lillian', '02ddc33ff68976936ad9c705033b7a5515feed1fbefca02f49ad660155b879e3', 2, 67, 'GIN'),
    ('SLKES', 'Sloan Kessie', 'c98304f000a474ad646e72a2984f9c85234766be1c5a4db79138e7b5ae409bb2', 8, 88, 'GCH'),
    ('MOANN', 'Moll Anne', 'c2fe4fc543f73c5f433f3fbeb8fb48b7a3ab8958ec16a28c98d7798b81d98823', 9, 41, 'GMC'),
    ('XAKAI', 'Xavier Kaitlin', '98bf5c20d4ca3de1f07b722122b291572be8447bc0bd285662837e26d97fc2b9', 3, 1, 'GEX'),
    ('TAAMA', 'Taylo Amaya', '8ac173f867d9551b22f176c78fd20f3421b5baacf77debe4cbab9ae26bf23920', 1, 114, 'GPH'),
    ('JOCLE', 'Jolen Cleo', '28d53f0d83154b4932373d5587c0ae7f00626ff5667eb2cd7a5e872e35b5afb6', 7, 56, 'GEL'),
    ('LYORL', 'Lysandr Orla', '944f8ea8851a910d029cda4babb45eaa152a80a3ec3b248ff4f3a7a187d7e206', 9, 86, 'GMN'),
    ('SAKYL', 'Samanth Kylie', '6bef9f6fdc343758f6a5f1e8646fb91276ea811ee444044c72d97c3d5ef42814', 4, 60, 'ENV'),
    ('JOFAL', 'Jo Fallon', '289cd6e93df8af0af0b21b941125ad9a8e372f54ea122e931f7e45917d842529', 4, 17, 'GEL'),
    ('ALKIR', 'Alexandr Kirsten', '26f028e1ed3da88522f56e2b70651570fbdec16a5d59e2cab23e376646b50e71', 0, 119, 'GCI'),
    ('SHCHA', 'Sha Charissa', 'cb39ec51e91ec950972a960b5fdf935c99611b0e676db2629e66b53e7df8c28b', 7, 45, 'GIN'),
    ('RACAL', 'Ram Calista', 'fddce4f3fe6d5c7e81b1ffe9cab7ff577f5de03d6e8e70420adfb4f01a79d898', 7, 38, 'GEL'),
    ('LADES', 'Lac Destiny', '5499c86682a617a6accef7f62ad5856e0f7ebb729ca424f850a8d6326af55497', 1, 53, 'GMN'),
    ('UNTAN', 'Unit Tanisha', '5878fff0deed45ad94aff5a1bc50b19e51023062d0729363f6d26bba5647cfc1', 2, 4, 'GCH'),
    ('LELEA', 'Le Leah', 'd7e10f38baee967a9fcdc58234d565632242d3d5c511e84825195562b72e882f', 9, 95, 'GEL'),
    ('CAING', 'Camero Inga', 'e72bb62be79d9cface60cd3b25b84ea44efe12b00e7e550c94393d7c5e1715a9', 7, 47, 'ENV'),
    ('REDES', 'Reaga Destiny', '9e9d90ef7bc90419bc06c45e7b45aa8b6f52d3861152627d21e5511926751bfa', 6, 52, 'GLO'),
    ('INANG', 'Indig Angela', '3e9638dee8f0af4513bda581a20c3ef4fc7395b40452dd7cd08ffc1f710b6687', 7, 6, 'GLO'),
    ('NESHE', 'Nell Shea', '6ac3445ec0864d79015a5e57481d6fe6eb714e4ad4372ec2b2bda7ef649a1522', 5, 44, 'GMC'),
    ('DAFAY', 'Daphn Fay', '5832500699d0e64eb5b661decde1bd4ed0ea07a2b41100c1f47e33390b49f9cd', 8, 6, 'GCH'),
    ('WHINA', 'Whilemin Ina', '3d98720c198e598db9cfba99e60b590269548b08c0af68f2b4925ba6359dee7f', 1, 95, 'GPH'),
    ('YAUMA', 'Yae Uma', '7e73d6220824fadd445cab01a8c2a5adb21e0dc6240c7102a566c9e9def3eb1f', 7, 96, 'GIN'),
    ('ELCAR', 'Ell Carolyn', '56d1f62e842b66d45673f0f2e6400127714a873e79616b5357f483aa2b189dff', 1, 112, 'GCH'),
    ('RYHAR', 'Ryle Harriet', '3bcdced390432bdc77ce626b04057267e45006f454b7611414c9f87c3c7ba898', 6, 83, 'GPH'),
    ('LAAMA', 'Lavini Amanda', 'e200982de09ddbd3235988c83193abc7bf33ba7b105e4af84ea1e49529dcf9a0', 9, 102, 'GMN'),
    ('LADEB', 'Laure Debra', '190af3596c7d443801c05520d0080626e0cfe33a6be3b77a6fc564f7470972e7', 7, 97, 'GEX'),
    ('ADDOR', 'Adrienn Dora', 'ed8a22c73e5cd7530783a05abe67b8461f4704b96fd1287af792b44f0dd8997c', 0, 99, 'ENV'),
    ('GRGAL', 'Gretche Galena', 'a2c54c990edb72ab50ee87ccc9a05d464f957218afa51379f6e3770b3069825a', 0, 100, 'GCH'),
    ('MOLES', 'Moll Lesley', '01b8eaaf5053e8ea5b5cd8f9e0b31a8ffee4e82156c594170a076a07f90f3f79', 7, 30, 'GLO'),
    ('LYGIN', 'Lysandr Ginger', '32b3dbc5489b6b20015b491cc7691f165eb686be89085165150c8df43b9e2579', 2, 72, 'GGL'),
    ('LYKEE', 'Lyn Keelie', '6d4b94a9933f713e5ba6b74c5633aa39f9b77b91ee4a415da91cc59d534cc8d5', 6, 75, 'GMC'),
    ('ARCAM', 'Arian Camille', 'b3a897937733c30533a574b978a55f9b95cd4362c82c2cd37d8c97d01c15ec3f', 9, 78, 'GEL'),
    ('AMAYA', 'Amen Ayanna', 'f6f869b0977414470e42a03b56bc61a527bafb39d51abc2d50f5213ed3e6c538', 5, 93, 'ENV'),
    ('MARUT', 'Marik Ruth', 'a41099b45d280b05ac283abbf7811496ac02ee4d79f7911c5576d789b33e4960', 0, 99, 'ENV'),
    ('TEFAY', 'Teaga Fay', '2a804631009b96ec2f338e8e84de640b2d9b1d686f8e820dcf058fcaaaeb4ef0', 2, 90, 'GEL'),
    ('FELIL', 'Felici Lila', '7aadf1ba2d224d891e4909114146437d87bf714062c17c38cfdf5b5f5d0ab337', 8, 53, 'GIN'),
    ('OLING', 'Olg Inga', '7599b770c732a7f55761e5bb2e3005fe6b32550dce1e508b40cc97a3f5a3661a', 4, 77, 'GEX'),
    ('INCOU', 'Indir Courtney', '737f33617d3fcf6f030e43439f846883f1d4377068bba22df3ba1b00b8634d92', 7, 82, 'GCH'),
    ('KIBRI', 'Kimberl Britanni', 'a5bf726ca11b3be05841f01fecd7d6237a7fa67a65e4f5085cb5786236524459', 8, 104, 'GCH'),
    ('MACHR', 'Mac Christen', '8d7fce3f84f94021b369408782507091c85ad43d67cea2ecc39259bd1d12aff0', 7, 86, 'GEL'),
    ('BRMAL', 'Brittan Mallory', 'f8b6b02b2447a46084718936f47b7c6d830659baa2d3dfa37b82ec6e9b4ada5c', 9, 52, 'GIF'),
    ('LASHA', 'Latifa Shay', '7b62828ffc7d85339ed37aa7dc11fe5c9915bde4daa3238678f557da59462604', 4, 117, 'GEX'),
    ('RACOU', 'Ran Courtney', 'a48c3ae2b6e6c3aeb4b6cf32b7fd27cc44887c76d5355b81d5ef8be5fab670be', 5, 107, 'GPH'),
    ('BELIL', 'Be Lila', '6d16b47e970c1308d237705096160748e972f7b1647c82de0f5ea763998cd99e', 4, 111, 'GMN');

INSERT INTO Service(id, nom, disponible, sigleProgramme)
	VALUE
	(1235, 'CDA',1, 'GLO'),
	(1234, 'SPLA',0, 'GLO'),
	(3366, 'CARRE',1, 'GLO'),
	(3466, 'Gestion des études',0, 'GLO'),
	(4143, 'Gestion des études',1, 'GLO');
INSERT INTO directeur(mail, nom, numeroTelephone, sigleProgramme)
	VALUE
	('Brahim.Chaib-draa@ift.ulaval.ca',  'Brahim Chaib-draa', '418 656-2131 poste 403346', 'GLO');
INSERT INTO Objectif(idul,id, sessions, nom, concentration, moyenneSession, moyenneFinProgramme, moyenneCours, sigleProgramme)
	VALUE
	('RACOU', 1,  'Hiver', 'Tout Peter', 'Traitement de donnee Massive', 3, 3.45, 4, 'GLO'),
	('RACOU', 2, 'Hiver', 'Tout Peter', 'Traitement de donnee Massive', 3, 3.45, 4, 'GLO');

INSERT INTO Cours(sigleCours, nom, credit, evaluation)
	VALUE
	('MAT-1910',  'Math de ingenieur I', 3, 4);

INSERT INTO Concentration(id, nom, sigleProgramme)
    Value
    (122, 'Traitement de donnees massive', 'GLO');

INSERT INTO Appartient(id, sigleProgramme, sigleCours,typeCours,disponibilite, regle, creditRegle)
    Value
    (123, 'GLO', 'GLO-4027', 'o', 'H', '3', '9');

INSERT INTO Suivre(idul, sigleCours, sessions, moyenne)
	VALUE
	('GAJAC',  'MAT-1910', 'Hiver', 3);

/*
CREATE TABLE Emprunts(
	cote smallint,
	pret date,
	retour date,
	id smallint,
	PRIMARY KEY(cote, pret),
	FOREIGN KEY(cote) REFERENCES Copies(cote) ON DELETE CASCADE,
	FOREIGN KEY(id) REFERENCES Utilisateurs(id) ON DELETE CASCADE
	);

INSERT INTO Suivre(idul, sigleCours, sessions, moyenne)
	VALUE
	('DIBAX',  'MAT-1910', 'Hiver', 3);
	
INSERT INTO Copies(cote, isbn, disponible)
	VALUE
	(0, 1234, 1),
	(1, 1234, 0),
	(2, 1234, 0),
	(3, 2345, 0),
	(5, 4567, 1),
	(6, 5678, 0),
	(7, 5678, 0),
	(8, 6789, 1),
	(9, 7890, 0);
	
INSERT INTO Utilisateurs(id, nom, adresse, age)
	VALUE
	(10, 'Alice', '2020 Rue Finfin', 25),
	(20, 'Bob', '1111 Premiere Avenue', 7),
	(30, 'Cedric', '42 Rue de la Reponse', 15),
	(40, 'Denise', '1234 Avenue Croissante', 43),
	(50, 'Frank', '3 Carre du Pentagone', 5),
	(60, 'Gerard', '2020 Rue Finfin', 32),
	(70, 'Henry', '39 Avenue Khoury', 12);
	
INSERT INTO Emprunts (cote, pret, retour, id)
	VALUE
	(0, '2017-01-05', '2017-02-07', 10),
	(0, '2017-05-18', '2017-06-19', 30),
	(0, '2018-11-15', '2018-12-18', 50),
	(1, '2015-02-04', '2015-04-01', 10),
	(1, '2015-06-08', '2015-08-02', 20),
	(1, '2016-04-01', '2016-05-13', 40),
	(1, '2017-03-15', '2017-08-02', 30),
	(1, '2018-11-14', '2018-12-06', 70),
	(1, '2018-12-20', '2019-02-13', 60),
	(2, '2017-05-04', '2017-06-08', 50),
	(2, '2018-06-03', '2018-09-12', 30),
	(2, '2018-11-15', '2018-12-09', 60),
	(3, '2019-01-14', '2019-03-15', 60),
	(4, '2014-02-13', '2014-05-18', 40),
	(5, '2015-03-12', '2015-05-17', 10),
	(6, '2015-04-12', '2015-06-17', 30),
	(6, '2016-06-19', '2016-06-21', 20),
	(6, '2018-12-15', '2019-01-17', 70),
	(7, '2018-09-18', '2018-11-10', 50),
	(7, '2019-02-14', '2019-03-15', 20),
	(8, '2017-05-04', '2017-06-19', 30),
	(9, '2018-09-15', '2018-11-16', 60),
	(9, '2017-04-16', '2017-05-12', 10);
    fgoshgiuhteaiugh
    */