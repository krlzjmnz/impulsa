/*
 Navicat Premium Data Transfer

 Source Server         : Always
 Source Server Type    : MySQL
 Source Server Version : 110413 (11.4.13-MariaDB)
 Source Host           : mysql-krlz.alwaysdata.net:0
 Source Schema         : krlz_impulsa_db

 Target Server Type    : MySQL
 Target Server Version : 110413 (11.4.13-MariaDB)
 File Encoding         : 65001

 Date: 02/11/2026 11:51:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for PRODUCTO
-- ----------------------------
DROP TABLE IF EXISTS `PRODUCTO`;
CREATE TABLE `PRODUCTO`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `unidadMedida` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `precioDistribuidor` float(7, 2) NULL DEFAULT NULL,
  `precioMenudeo` varchar(7) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `pv` float(6, 2) NULL DEFAULT NULL,
  `sv` float(6, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 118 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of PRODUCTO
-- ----------------------------
INSERT INTO `PRODUCTO` VALUES (1, 'FB005', 'DNX Roselle juice 285ml', 'concentrado de jamaica', '1 Botella x 285ml', 355.00, '533.00', 5.50, 134.00);
INSERT INTO `PRODUCTO` VALUES (2, 'FB027', 'DXN Morinzhi', 'jugo de noni - morinzhi', '1 Botella x 285ml', 385.00, '578.00', 5.50, 170.00);
INSERT INTO `PRODUCTO` VALUES (3, 'FB032', 'Morinzyme', 'Concentrado de noni fermentado', '1 Botella x 285ml', 385.00, '578.00', 5.50, 170.00);
INSERT INTO `PRODUCTO` VALUES (4, 'FB032', 'DXN Spirulina Cereal', 'Cereal con espirulina', '30 Sobres x 30 gr', 860.00, '1290.00', 15.60, 395.00);
INSERT INTO `PRODUCTO` VALUES (5, 'FB034', 'DXN Zhi Mocha', 'Café Zhi Mocha', '20 Sobres x 21gr', 495.00, '743.00', 6.50, 198.00);
INSERT INTO `PRODUCTO` VALUES (6, 'FB044', 'DXN Nutrizhi', 'Polvo para preparar bebida de soya, Malta y Ganoderma', '20 Sobres x 30 gr', 495.00, '743.00', 9.50, 228.00);
INSERT INTO `PRODUCTO` VALUES (7, 'FB057', 'DXN Kiwi Fruit Drink Base', 'Concentrado de Kiwi para preparar bebida', '1 Botella x 1L', 615.00, '923', 10.00, 239.00);
INSERT INTO `PRODUCTO` VALUES (8, 'FB063', 'DXN Zhi Cafe Classic', 'Cafe mezclado con extracto de ganodermo', '20 Sobres x 20gr', 430.00, '645.00', 5.50, 151.00);
INSERT INTO `PRODUCTO` VALUES (9, 'FB066', 'DXN Lingzhi Coffe 3 en 1 Lite', 'DXN Lingzhi Coffe 3 en 1 Lite', '20 sobres x 21 gr', 380.00, '570.00', 4.60, 131.00);
INSERT INTO `PRODUCTO` VALUES (10, 'FB067', 'DXN Vinaigette 285 ml', 'Concentrado para preparar bebida de vinagre de arroz y Ganoderma', '1 Botella x 285 ml\r\n1 Botella x 285 ml\r\n1 Botella x 285 ml\r\n1 Botella x 285 ml\r\n', 370.00, '555', 4.60, 131.00);
INSERT INTO `PRODUCTO` VALUES (11, 'FB068', 'DXN Cream Coffe', 'Polvo para preparar bebida con café y extracto de Ganoderma', '20 Sobres x 14 gr', 460.00, '690.00', 5.90, 161.00);
INSERT INTO `PRODUCTO` VALUES (12, 'FB069', 'DXN Cordyceps Cereal', 'Cereal con Cordyceps', '20 Sobres x 30 gr', 1000.00, '1500.00', 23.00, 261.00);
INSERT INTO `PRODUCTO` VALUES (13, 'FB089', 'DXN Pineapple Jam', 'Mermelada de piña con extracto de Ganoderma', '1 Frasco x 400 gr', 240.00, '360.00', 3.00, 100.00);
INSERT INTO `PRODUCTO` VALUES (14, 'FB120', 'DXN Fruzim', 'Concentrado de durazno y ciruela fermentados', '1 Botella x 380 ml', 460.00, '690.00', 7.40, 179.00);
INSERT INTO `PRODUCTO` VALUES (15, 'FB121', 'DXN Spica Tea ', 'Té Spica', '20 Bolsitas x 5 gr', 455.00, '683.00', 5.50, 205.00);
INSERT INTO `PRODUCTO` VALUES (16, 'FB129', 'DXN Cordyceps Coffee 3 in 1', 'Café con Cordyceps', '20 Paquetes x 21 gr', 430.00, '645.00', 5.00, 148.00);
INSERT INTO `PRODUCTO` VALUES (17, 'FB143', 'DXN Zhi Mint Plus', 'Zhi Mint Plus', '12 Sobres x 25 gr', 895.00, '1343.00', 12.00, 309.00);
INSERT INTO `PRODUCTO` VALUES (18, 'FB146', 'Lingzhi Coffee 3 in 1', 'Café Lingzhi 3 en 1', '20 Sobres x 21 gr', 345.00, '518.00', 4.60, 138.00);
INSERT INTO `PRODUCTO` VALUES (19, 'FB147', 'Lingzhi Black Coffee ', 'Café Lingzhi Negro 2 en 1', '20 Sobres x 4.5 gr ', 345.00, '518.00', 4.60, 138.00);
INSERT INTO `PRODUCTO` VALUES (20, 'FB148', 'Vita Café', 'Polvo para preparar bebida de café con ginseng, tongkat ali y extracto de Ganoderma', '20 Sobres x 21 gr', 430.00, '645.00', 6.20, 160.00);
INSERT INTO `PRODUCTO` VALUES (21, 'FB149', 'Cocozhi', 'Bebida de cocoa - Cocozhi', '20 Sobres x 32 gr', 415.00, '623.00', 6.00, 205.00);
INSERT INTO `PRODUCTO` VALUES (22, 'FB150', 'DXN Civattino Coffee', 'Café Civattino', '1 Frasco x 200 gr', 1985.00, '2978.00', 38.40, 794.00);
INSERT INTO `PRODUCTO` VALUES (23, 'FB151', 'DXN L-Vegmix', 'Mezcla de vegetales y dátiles deshidratados', '10 Paquetes x 27 gr', 615.00, '923.00', 8.70, 246.00);
INSERT INTO `PRODUCTO` VALUES (24, 'FB152', 'DXN Ganoderma Mushroom 100g ', 'Hongo Ganoderma DXN', '1 Botella x 100 gr', 570.00, '855.00', 6.40, 225.00);
INSERT INTO `PRODUCTO` VALUES (25, 'FB155', 'DXN Lemonzhi', 'Polvo para preparar bebida de té negro con limón y extracto de Ganoderma', '20 Sobres x 22 gr', 285.00, '428.00', 4.70, 111.00);
INSERT INTO `PRODUCTO` VALUES (26, 'FB161', 'DXN White Coffee Zhino', 'Café Blanco Zhino', '12 Sobres x 28 gr', 475.00, '713.00', 7.00, 168.00);
INSERT INTO `PRODUCTO` VALUES (27, 'FB179', 'DXN Lignopine 285ml', 'Jugo De Piña con Lignosus Rhinocerus Lignopine', '1 Botella x 285 ml', 1225.00, '1838.00', 17.00, 535.00);
INSERT INTO `PRODUCTO` VALUES (28, 'FB189', 'DXN Cin-G', NULL, '5 Paquetes x 60 gr', 475.00, '713.00', 6.10, 214.00);
INSERT INTO `PRODUCTO` VALUES (29, 'FB206', 'DXN Apple Enzyme Drink ', 'Bebida de Jugo de Manzana fermentada', '15 Paquetes x 50 ml ', 885.00, '1328.00', 14.00, 382.00);
INSERT INTO `PRODUCTO` VALUES (30, 'FB219', 'DXN Aloe Vita ', 'Bebida de Aloe Vera', '1 Botella x 285 ml', 195.00, '293.00', 3.00, 76.00);
INSERT INTO `PRODUCTO` VALUES (31, 'FB223', 'DXN Zhitea', 'Premezcla de té', '1 Botella x 100 gr', 445.00, '668.00', 5.50, 190.00);
INSERT INTO `PRODUCTO` VALUES (32, 'FB229', 'DXN Oocha', 'Polvo para preparar bebida con té oolong y extracto de Ganoderma', '12 Sobres x 30 gr', 525.00, '788.00', 7.00, 213.00);
INSERT INTO `PRODUCTO` VALUES (33, 'FB231', 'DXN Komb-B 285ml ', 'Bebida sabor a té fermentado Camelia sinensis) con 0.4% de mora', '1 Botella x 285 ml', 150.00, '225.00', 2.20, 59.00);
INSERT INTO `PRODUCTO` VALUES (34, 'FB232', 'DXN Lingzhi Tea Latte', 'Lingzhi Té Latte', '12 Sobres x 30 gr ', 525.00, '788.00', 7.00, 219.00);
INSERT INTO `PRODUCTO` VALUES (35, 'FB237', 'DXN Apple Fermented Jam', 'Mermelada de Manzana fermentada', '20 Paquetes x 15 gr', 270.00, '405.00', 4.60, 108.00);
INSERT INTO `PRODUCTO` VALUES (36, 'FB261', 'DXN Moricinia 285ml', 'Concentrado de noni y asam gelugur', '1 Botella x 285 ml', 385.00, '578.00', 5.50, 170.00);
INSERT INTO `PRODUCTO` VALUES (37, 'FB285', 'DXN Neph-V 285ml', 'Concentrado para preparar bebida de vinagre de rambután y Ganoderma Lucidum', '1 Botella x 285 ml', 455.00, '683', 5.80, 195.00);
INSERT INTO `PRODUCTO` VALUES (38, 'FB303', 'DXN VCO-L 285ml', 'Aceite comestible puro de coco virgen añadido con Ganoderma Lucidum ', '1 Botella x 285 ml', 815.00, '1223.00', 13.00, 280.00);
INSERT INTO `PRODUCTO` VALUES (39, 'FB304', 'DXN Roselle Juice 50ml', 'Concentrado de Jamaica para preparar bebida', '15 Paquetes x 50 gr', 1030.00, '1545.00', 15.80, 391.00);
INSERT INTO `PRODUCTO` VALUES (40, 'FB307', 'DXN Florathemum', 'Té de Aceitilla 60g', '1 Botella x 60 gr', 515.00, '773.00', 7.90, 220.00);
INSERT INTO `PRODUCTO` VALUES (41, 'FB308', 'DXN Oozhi Tea 100g', 'Mezcla de Té de Oolong con Ganoderma Lucidum 100g', '1 Botella x 100 gr', 425.00, '638.00', 6.40, 161.00);
INSERT INTO `PRODUCTO` VALUES (42, 'FB315', 'DXN Lion’s Mane Lemon Matcha', 'Polvo para preparar bebida de mezcla de limón, té negro, té Oolong y hongo melena de león', '20 Sobres x 22 gr', 395.00, '593.00', 5.50, 137.00);
INSERT INTO `PRODUCTO` VALUES (43, 'FB336', 'DXN Multipurpose Seasoning', 'Sazonador de alimentos', '1 Botella x 120 gr', 435.00, '635.00', 5.10, 162.00);
INSERT INTO `PRODUCTO` VALUES (44, 'FB337', 'DXN Jujube Fruits', 'Dátiles rojos chinos', '1 Bolsa = 300 gr', 280.00, '420.00', 4.00, 99.00);
INSERT INTO `PRODUCTO` VALUES (45, 'FB345', 'DXN Goji Berries ', 'Bayas de goji', '1 Bolsa = 350 gr', 735.00, '1103.00', 11.50, 257.00);
INSERT INTO `PRODUCTO` VALUES (46, 'FB351', 'DXN Oozhi Tea 30g', 'Mezcla de té Oolong con Ganoderma Lucidum', '1 Botella x 30 gr', 150.00, '225.00', 2.40, 57.00);
INSERT INTO `PRODUCTO` VALUES (47, 'FB352', 'DXN Oozhi Tea (30s)', 'Caja con 30 sobres', '30 Sobres x 1 gr', 185.00, '278.00', 2.90, 71.00);
INSERT INTO `PRODUCTO` VALUES (48, 'FB360', 'DXN SUGAR', 'Azúcar Blanca', '30 paquetes x 5 gr ', 145.00, '218.00', 0.60, 51.00);
INSERT INTO `PRODUCTO` VALUES (49, 'FB362', 'DXN Oolong Tea Powder 30g ', 'DXN Oolong Tea Powder 30g ', '1 Botella x 30 gr', 275.00, '413.00', 4.10, 119.00);
INSERT INTO `PRODUCTO` VALUES (50, 'FB364', 'DXN Zhi Roasted Coffee', 'Café premezclado con extracto de ganoderma', '30 Sobres x 4 gr', 325.00, '488.00', 5.40, 130.00);
INSERT INTO `PRODUCTO` VALUES (51, 'FB369', 'DXN Ootea Lingzhi Coffee Mix 3 in 1', 'Polvo para preparar bebida de café con té Oolong y extracto de Ganoderma', '20 Sobres x 21 gr', 345.00, '518', 5.90, 138.00);
INSERT INTO `PRODUCTO` VALUES (52, 'FB370', 'DXN Ootea Lingzhi Coffee Mix 3 in 1 Lite', 'Polvo para preparar bebida de café con té Oolong y extracto de Ganoderma', '20 Sobres x 21 gr', 325.00, '488.00', 5.90, 131.00);
INSERT INTO `PRODUCTO` VALUES (53, 'FB371', 'Ootea Lingzhi Coffee Mix 2 in 1', 'Polvo para preparar bebida de café con té Oolong y extracto de Ganoderma', '20 Sobres x 11 gr', 370.00, '555.00', 5.60, 148.00);
INSERT INTO `PRODUCTO` VALUES (54, 'FB372', 'Ootea Cordyceps Coffee Mix 3 in 1 (', 'Polvo para preparar bebida de café con té Oolong y Cordyceps', '20 Paquetes x 21 gr', 370.00, '555.00', 5.90, 150.00);
INSERT INTO `PRODUCTO` VALUES (55, 'FB375', 'DXN Ootea Lingzhi Black Coffee Mix', 'Polvo para preparar bebida de café con té Oolong y extracto de Ganoderma', '20 Sobres x 4.5 gr', 345.00, '518.00', 5.90, 138.00);
INSERT INTO `PRODUCTO` VALUES (56, 'FB443', 'DXN Apple Sparkling Drink', 'Refresco con 29% de concentrado de manzana fermentada', '1 Botella x 330 ml', 90.00, '135.00', 1.00, 31.00);
INSERT INTO `PRODUCTO` VALUES (57, 'FB446', 'DXN Lion’s Mane Black Coffee Drink', 'Bebida de café con 0.6%  de hongo de melena de león (Hericium erinaceus)', '1 Botella x 330 ml', 100.00, '135.00', 1.10, 35.00);
INSERT INTO `PRODUCTO` VALUES (58, 'FB539', 'DXN Ootea Zhi Mocha Mix', 'Polvo para preparar bebida de café de café con cocoa, té Oolong y extracto de Ganoderma', '20 sobres x 21 g', 495.00, '743.00', 7.10, 198.00);
INSERT INTO `PRODUCTO` VALUES (59, 'FB540', 'DXN Ootea Eucafe Mix', 'Polvo para preparar bebida de café con té Oolong y tongkat ali', '20 sobres x 21 g', 355.00, '533.00', 6.30, 144.00);
INSERT INTO `PRODUCTO` VALUES (60, 'FB541', 'DXN Ootea White Coffee Zhino Mix', 'Polvo para preparar preparar bebida de café con té Oolong y extracto de Ganoderma', '12 sobres x 28 g ', 410.00, '615.00', 7.40, 168.00);
INSERT INTO `PRODUCTO` VALUES (61, 'FB620', 'DXN Ootea Vita Cafe Mix', 'Polvo para preparar bebida de café con té Oolong, ginsen, tongkat ali y extracto de ganoderma', '20 Sobres x 21 g', 370.00, '555.00', 7.40, 160.00);
INSERT INTO `PRODUCTO` VALUES (62, 'HA012', 'DXN Tea Infuser ', 'DXN infusor de té', '1 Unidad', 445.00, '668', 7.60, 154.00);
INSERT INTO `PRODUCTO` VALUES (63, 'HF002', 'RG 30', 'Reishi Gano 30 Cápsulas', '30 Cápsulas x 270 mg', 345.00, '518.00', 5.80, 136.00);
INSERT INTO `PRODUCTO` VALUES (64, 'HF004', 'GL 30', 'Ganocelium 30 Cápsulas', '30 Cápsulas x 450 mg', 345.00, '518.00', 5.80, 136.00);
INSERT INTO `PRODUCTO` VALUES (65, 'HF022', 'DXN Bee Pollen Tablets 120’s', 'DXN Bee Pollen 120 Tabletas', '120 Tabletas x 300 mg', 575.00, '863.00', 8.00, 227.00);
INSERT INTO `PRODUCTO` VALUES (66, 'HF024', 'DXN Cordyceps Capsules 60’s ', 'DXN Cordyceps 60 Cápsulas', '60 Cápsulas x 450 mg ', 1605.00, '2408.00', 25.00, 625.00);
INSERT INTO `PRODUCTO` VALUES (67, 'HF029', 'DXN Lion’s Mane Tablets 120’s', 'DXN Lions Mane 120 Tabletas', '120 Tabletas x 300 mg ', 610.00, '915.00', 10.00, 254.00);
INSERT INTO `PRODUCTO` VALUES (68, 'HF031', 'Spirulina Tablet 120’s', 'Espirulina 120 Tabletas', '120 Tabletas x 250 mg', 370.00, '555.00', 5.00, 149.00);
INSERT INTO `PRODUCTO` VALUES (69, 'HF036', 'DXN Spirulina Capsule 30’s ', 'DXN Espirulina 30 Cápsulas', '30 Cápsulas x 350 mg', 140.00, '210', 2.20, 56.00);
INSERT INTO `PRODUCTO` VALUES (70, 'HF037', 'DXN Spirulina Capsule 90’s ', 'DXN Espirulina 90 Cápsulas', '90 Cápsulas x 350 mg', 405.00, '608.00', 6.30, 164.00);
INSERT INTO `PRODUCTO` VALUES (71, 'HF049', 'DXN Black Cumin Plus Capsule 30’s', 'DXN Black Cumin Plus 30 Cápsulas', '30 Cápsulas x 350 mg', 475.00, '713.00', 7.70, 221.00);
INSERT INTO `PRODUCTO` VALUES (72, 'HF053', 'DXN Monascus Capsule 30’s', 'DXN Monascus 30 Cápsulas', '30 Cápsulas x 450 mg', 500.00, '750.00', 7.70, 234.00);
INSERT INTO `PRODUCTO` VALUES (73, 'HF060', 'DXN Spirulina Capsule 360’s', 'DXN Espirulina 360 Cápsulas', '360 Cápsulas x 350 mg', 1540.00, '2310.00', 23.60, 632.00);
INSERT INTO `PRODUCTO` VALUES (74, 'HF066', 'DXN Spirulina Powder 50g', 'DXN Espirulina en polvo 50g', '1 Botella x 50 g', 560.00, '840.00', 8.80, 226.00);
INSERT INTO `PRODUCTO` VALUES (75, 'HF095', 'DXN Gegen Plus Powder ', 'DXN Gegen Plus en polvo 30g', '1 Botella x 30 g', 700.00, '1050.00', 11.80, 289.00);
INSERT INTO `PRODUCTO` VALUES (76, 'HF096', 'DXN Gengen plus Capsule 30\'s', 'DXN  Gengen plus 30 capsulas', '30 Cápsulas x 350 mg', 295.00, '443', 5.00, 121.00);
INSERT INTO `PRODUCTO` VALUES (77, 'HF097', 'DXN Gegen Plus Capsule 90’s ', 'DXN Gegen Plus 90 Cápsulas', '90 Cápsulas x 350 mg ', 815.00, '1223.00', 13.70, 336.00);
INSERT INTO `PRODUCTO` VALUES (78, 'HF102', 'DXN Ros L Powder 30g', 'DXN Ros L en polvo 30g', '1 Botella x 30 gr', 295.00, '443.00', 5.00, 115.00);
INSERT INTO `PRODUCTO` VALUES (79, 'MXKITA', 'Basic Kit', 'Kit básico', '1 SET', 450.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (80, 'MXKIT2A', 'Membership Kit with Lingzhi Coffee 3 in 1', 'Kit de Membresía con café Lingzhi 3 en 1', '1 SET', 770.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (81, 'PC004', 'Shampoo Ganozhi ', 'Ganozhi Shampoo', '1 Botella x 250 ml ', 420.00, '630.00', 5.00, 183.00);
INSERT INTO `PRODUCTO` VALUES (82, 'PC005', 'Gel de Baño Ganozhi', 'Ganozhi Body Foam', '1 Botella x 250 ml', 420.00, '630.00', 5.00, 183.00);
INSERT INTO `PRODUCTO` VALUES (83, 'PC006', 'Pasta de Dientes Ganozhi', 'Ganozhi Toothpaste', '1 Tubo x 150 gr', 230.00, '345.00', 3.00, 94.00);
INSERT INTO `PRODUCTO` VALUES (84, 'PC007', 'Aceite de Masaje Gano ', 'Gano Massage Oil', '1 Botella x 75 ml', 310.00, '465.00', 3.80, 144.00);
INSERT INTO `PRODUCTO` VALUES (85, 'PC015', 'DXN Talcum Powder', 'Talco en Polvo', '1 Botella x 250 gr ', 240.00, '360.00', 3.00, 96.00);
INSERT INTO `PRODUCTO` VALUES (86, 'PC036', 'Jabón Ganozhi ', 'DXN Ganozhi Soap', '1 Barra x 80 gr', 130.00, '195.00', 1.50, 43.00);
INSERT INTO `PRODUCTO` VALUES (87, 'PC041', 'Cepillo Dental DXN (Adulto) ', 'DXN Toothbrush (For Adults', 'I pza', 130.00, '195.00', 1.50, 43.00);
INSERT INTO `PRODUCTO` VALUES (88, 'PC042 ', 'Cepillo Dental DXN (Infantil) ', 'DXN Toothbrush (For Children)', '1 pza', 130.00, '195.00', 1.50, 43.00);
INSERT INTO `PRODUCTO` VALUES (89, 'PC057', 'DXN Zhicare Toothpaste', 'Zhicare Pasta De Diente Ganozhi', '1 Tubo x 100 gr ', 320.00, '480.00', 3.20, 111.00);
INSERT INTO `PRODUCTO` VALUES (90, 'PC073', 'DXN Ganozhi Trans Soap', 'Jabón con Ganoderma lucidum', '1 Barra x 120 gr', 250.00, '375.00', 3.40, 87.00);
INSERT INTO `PRODUCTO` VALUES (91, 'PC074', 'DXN Oocha Trans Soap', 'Jabón Oocha Trans', '1 Barra x 120 gr', 250.00, '375.00', 3.40, 87.00);
INSERT INTO `PRODUCTO` VALUES (92, 'SC009 ', 'DXN Ganozhi Toner', 'Tónico Facial', '1 Botella x 150 ml', 975.00, '1463.00', 12.50, 385.00);
INSERT INTO `PRODUCTO` VALUES (93, 'SC010\r\n', 'DXN Ganozhi Moisturizing Micro Emulsion', 'Emulsión Facial', '1 Botella x 50 ml', 1285.00, '1928.00', 16.50, 505.00);
INSERT INTO `PRODUCTO` VALUES (94, 'SC011', 'DXN Ganozhi Liquid Cleanser', 'Limpiador Facial', '1 Botella x 150 ml ', 975.00, '1463.00', 12.50, 385.00);
INSERT INTO `PRODUCTO` VALUES (95, 'SC012', 'DXN Chubby Baby Oil ', 'Aceite para bebé', '1 Botella x 200 ml', 265.00, '398.00', 3.00, 105.00);
INSERT INTO `PRODUCTO` VALUES (96, 'SC014', 'DXN Ganozhi Lipstick - Coco Red ', 'Lápiz Labial Rojo Coco', '1 Tubo x 3.5 gr', 635.00, '953.00', 9.45, 251.00);
INSERT INTO `PRODUCTO` VALUES (97, 'SC015', 'DXN Ganozhi Lipstick - Pearly Red', 'Lápiz Labial Rojo Nacarado', '1 Tubo x 3.5 gr', 635.00, '953.00', 9.45, 251.00);
INSERT INTO `PRODUCTO` VALUES (98, 'SC017', 'DXN Ganozhi Lipstick - Pearly Grape ', 'Lápiz Labial Uva Nacarado', '1 Tubo x 3.5 gr', 635.00, '953.00', 9.45, 251.00);
INSERT INTO `PRODUCTO` VALUES (99, 'SC020', 'DXN Aloe. V Cleansing Gel ', 'Gel Limpiador Facial', '1 Tubo x 100 ml', 315.00, '473', 5.20, 124.00);
INSERT INTO `PRODUCTO` VALUES (100, 'SC021', 'DXN Aloe. V Hydrating Toner ', 'Tónico Hidratante Facial', '1 Botella x 100 ml', 315.00, '473.00', 5.20, 124.00);
INSERT INTO `PRODUCTO` VALUES (101, 'SC022', 'DXN Aloe. V Aqua Gel', 'Gel Hidratante Facial', '1 Tubo x 50 ml ', 400.00, '600.00', 6.00, 158.00);
INSERT INTO `PRODUCTO` VALUES (102, 'SC023', 'DXN Aloe V. Nutricare Cream', 'Crema Facial)', '1 Tubo x 30 ml', 400.00, '600.00', 6.00, 158.00);
INSERT INTO `PRODUCTO` VALUES (103, 'SC024', 'DXN Aloe V. Hand & Body Lotion', 'Loción para Manos y Cuerpo', '1 Botella x 250 ml', 315.00, '473.00', 5.20, 124.00);
INSERT INTO `PRODUCTO` VALUES (104, 'SC025', 'DXN Ganozhi Complete Skin Care Series Travel Kit', '(1 set Ganozhi Skin Care Series Travel Kit Package)\r\nGanozhi Liquid Cleanser\r\nGanozhi Moisturizing Micro Emulsion\r\nGanozhi Toner\r\nSkin Care Series Travel Kit Transparent PVC Bag', 'con Bolsa de PVC 1 Botella x 30 ml\r\n1 Botella x 15 ml\r\n1 Botella x 30 ml', 1045.00, '1568.00', 13.00, 412.00);
INSERT INTO `PRODUCTO` VALUES (105, 'SC026', 'DXN Ganozhi E Deep Cleansing Cream', 'Crema Limpiadora\r\nFacial', '1 Tubo x 120 g', 730.00, '1095.00', 10.80, 288.00);
INSERT INTO `PRODUCTO` VALUES (106, 'SC027', 'DXN Ganozhi E Hydrasoft Toner', 'Tónico Facial', '1 Botella x 120 ml', 750.00, '1125.0', 17.00, 470.00);
INSERT INTO `PRODUCTO` VALUES (107, 'SC028', 'DXN Ganozhi E UV Defense Day Cream', 'Crema Facial de Día', '1 Botella x 50 gr', 1195.00, '1793.0', 17.00, 470.00);
INSERT INTO `PRODUCTO` VALUES (108, 'SC029', 'DXN Ganozhi E Nourishing Night Cream', 'Crema Facial\r\nNocturna', '1 Botella x 50 g', 1245.00, '1868.0', 18.40, 490.00);
INSERT INTO `PRODUCTO` VALUES (109, 'SC032', 'DXN Aloe V. Facial Scrub ', 'Exfoliante Facial', '1 Tubo x 75 gr ', 360.00, '540.00', 5.80, 142.00);
INSERT INTO `PRODUCTO` VALUES (110, 'SC033', 'DXN Aloe V. Hydrating Mask ', 'Mascarilla Hidratante Facial', '1 Tubo x 100 gr', 405.00, '608.00', 6.60, 160.00);
INSERT INTO `PRODUCTO` VALUES (111, 'SC035', 'DXN Ganozhi Lipstick - Coral Pink ', 'Lápiz Labial Rosa Coral', '1 Tubo x 3.0 gr', 635.00, '953.00', 9.45, 251.00);
INSERT INTO `PRODUCTO` VALUES (112, 'S2030', 'Playera DXN “Un Mundo Un Mercado”', 'DXN T-Shirt “Un Mundo Un Mercado”', '1 pza', 342.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (113, 'S2035', 'Bolsa Ecológica ', 'Ecology Bag', '1 pza', 23.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (114, 'P2138', 'Dato’ Dr. Lim Siow Jin-Mi Camino con DXN', NULL, '1 pza', 256.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (115, 'P2184', 'Sunya-The Power That Drives DXN, DXN Spanish Version', 'Sunya- El poder que conduce DXN', '1 pza', 256.00, NULL, NULL, NULL);
INSERT INTO `PRODUCTO` VALUES (116, 'AP011', 'DXN Kimono (Dark Blue)', 'size XS', '1 Set', 1525.00, '2288.0', NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
