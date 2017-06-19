/*
Navicat MySQL Data Transfer
Source Host     : localhost:3306
Source Database : teacher
Target Host     : localhost:3306
Target Database : teacher
Date: 2017-06-08 18:54:43
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `status` int(1) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `id` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('0', '15603379607', '123123', '唐峥', '11111');
