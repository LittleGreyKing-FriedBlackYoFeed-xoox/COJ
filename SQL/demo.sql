/*
 Navicat Premium Data Transfer

 Source Server         : aliyun
 Source Server Type    : MySQL
 Source Server Version : 80028 (8.0.28)
 Source Host           : 47.109.155.118:3309
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 80028 (8.0.28)
 File Encoding         : 65001

 Date: 08/03/2025 10:35:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance_records_score
-- ----------------------------
DROP TABLE IF EXISTS `attendance_records_score`;
CREATE TABLE `attendance_records_score`  (
  `stu_number` int NULL DEFAULT NULL COMMENT '学生序号',
  `stu_id` bigint NOT NULL COMMENT '学生学号',
  `stu_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `stu_class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生班级',
  `one_score` double NULL DEFAULT NULL COMMENT '第一次成绩',
  `two_score` double NULL DEFAULT NULL COMMENT '第二次成绩',
  `three_sroce` double NULL DEFAULT NULL COMMENT '第三次成绩',
  `four_score` double NULL DEFAULT NULL COMMENT '第四次成绩',
  `five_score` double NULL DEFAULT NULL COMMENT '第五次成绩',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '考勤分数表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance_records_score
-- ----------------------------
INSERT INTO `attendance_records_score` VALUES (57, 20181203922, '王子康', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (1, 20191202255, '纪嘉俊', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (58, 20191202610, '段兴江', '2021软件工程2班', 100, 60, 80, 100, 100);
INSERT INTO `attendance_records_score` VALUES (2, 20201202139, '张子龙', '2021软件工程1班', 100, 66, 0, 80, 100);
INSERT INTO `attendance_records_score` VALUES (3, 20211200384, '严芊芊', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (59, 20211200385, '顾培皓', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (4, 20211200551, '曾繁一', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (60, 20211200553, '王宗祥', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (5, 20211200556, '王鑫', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (6, 20211200558, '王贵萱', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (7, 20211200584, '何彦莹', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (61, 20211200596, '于舒睿', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (62, 20211200598, '张杨', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (63, 20211200601, '孙欣欣', '2021软件工程2班', 100, 100, 100, 90, 100);
INSERT INTO `attendance_records_score` VALUES (8, 20211200602, '刘鑫宇', '2021软件工程1班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (9, 20211200605, '郑琳', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (64, 20211200606, '迟稼铭', '2021软件工程2班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (10, 20211200710, '汪康', '2021软件工程1班', 100, 100, 67, 90, 100);
INSERT INTO `attendance_records_score` VALUES (65, 20211200711, '章嘉劭', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (11, 20211200719, '王鹏', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (66, 20211201119, '王福龙', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (12, 20211201141, '闫政', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (13, 20211201148, '郭会发', '2021软件工程1班', 100, 100, 100, 67, 95);
INSERT INTO `attendance_records_score` VALUES (14, 20211201392, '孙可言', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (15, 20211201418, '刘陵', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (67, 20211201454, '何海兴', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (68, 20211201457, '赵旋', '2021软件工程2班', 100, 95, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (16, 20211201458, '焦海霞', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (17, 20211201483, '张含锋', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (69, 20211201659, '彭锦龙', '2021软件工程2班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (70, 20211201766, '李欣欢', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (71, 20211201785, '马乐晨', '2021软件工程2班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (72, 20211201793, '乔佳昕', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (18, 20211201803, '张士博', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (19, 20211201804, '葛怀睿', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (20, 20211201806, '刘帅博', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (21, 20211201849, '魏继瑶', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (73, 20211201867, '付陈瑶', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (22, 20211201874, '郭伟康', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (23, 20211201875, '王林超', '2021软件工程1班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (24, 20211201878, '杨嘉沐', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (74, 20211201890, '常宏伟', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (75, 20211201893, '韩森宇', '2021软件工程2班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (25, 20211201897, '张锐颀', '2021软件工程1班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (26, 20211201899, '刘子轩', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (76, 20211201900, '王腾鑫', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (77, 20211201902, '张睿泽', '2021软件工程2班', 100, 100, 100, 100, 80);
INSERT INTO `attendance_records_score` VALUES (27, 20211201903, '董美娇', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (28, 20211202068, '常松', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (78, 20211202069, '刘庆龙', '2021软件工程2班', 100, 100, 100, 100, 67);
INSERT INTO `attendance_records_score` VALUES (79, 20211202072, '邢子阳', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (29, 20211202073, '陈浩然', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (80, 20211202079, '祁明扬', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (81, 20211202081, '任靓', '2021软件工程2班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (30, 20211202083, '高铎', '2021软件工程1班', 100, 100, 100, 100, 66);
INSERT INTO `attendance_records_score` VALUES (82, 20211202090, '姚祥桐', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (83, 20211202095, '王雅鑫', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (31, 20211202101, '陈广硕', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (32, 20211202103, '张瑛琪', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (84, 20211202104, '耿唯瀚', '2021软件工程2班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (33, 20211202111, '张博', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (85, 20211202112, '李明哲', '2021软件工程2班', 100, 100, 67, 80, 100);
INSERT INTO `attendance_records_score` VALUES (34, 20211202125, '黄照凯', '2021软件工程1班', 100, 100, 67, 0, 75);
INSERT INTO `attendance_records_score` VALUES (86, 20211202312, '徐婷', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (35, 20211202326, '李俊兰', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (87, 20211202355, '支毅博', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (88, 20211202362, '赵佳乐', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (36, 20211202380, '李轩', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (89, 20211202487, '翟翱', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (37, 20211202495, '饶峰', '2021软件工程1班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (38, 20211202543, '罗民富', '2021软件工程1班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (39, 20211202705, '丁金洋', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (90, 20211202720, '张书通', '2021软件工程2班', 100, 100, 90, 100, 100);
INSERT INTO `attendance_records_score` VALUES (40, 20211202723, '田兆卓', '2021软件工程1班', 100, 100, 100, 100, 90);
INSERT INTO `attendance_records_score` VALUES (41, 20211202724, '王洪福', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (91, 20211202726, '李韩', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (92, 20211202730, '郭桐羽', '2021软件工程2班', 100, 100, 90, 100, 100);
INSERT INTO `attendance_records_score` VALUES (93, 20211202732, '张宇', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (94, 20211202744, '王祉桥', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (95, 20211202754, '刘扬', '2021软件工程2班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (42, 20211202759, '唐文勃', '2021软件工程1班', 100, 100, 67, 0, 85);
INSERT INTO `attendance_records_score` VALUES (96, 20211202822, '何通海', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (97, 20211202855, '任子豪', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (43, 20211202868, '孙艺慧', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (44, 20211202878, '涂泉源', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (98, 20211202881, '吴健南', '2021软件工程2班', 100, 100, 95, 100, 100);
INSERT INTO `attendance_records_score` VALUES (45, 20211202900, '陈梦飞', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (99, 20211202947, '许孙凯', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (100, 20211202948, '白明涛', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (46, 20211203012, '王冠涵', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (47, 20211203035, '卢平', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (48, 20211203038, '刘浩宇', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (101, 20211203042, '信帅权', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (102, 20211203047, '邓大卫', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (49, 20211203049, '尹春普', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (103, 20211203059, '刘思豪', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (104, 20211203089, '张义超', '2021软件工程2班', 100, 67, 0, 100, 100);
INSERT INTO `attendance_records_score` VALUES (105, 20211203091, '王格格', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (50, 20211203783, '张楠', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (106, 20211203792, '戴明东', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (107, 20211203974, '李涵', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (108, 20211203978, '栾凯越', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (51, 20211203980, '刘佳欣', '2021软件工程1班', 100, 67, 100, 85, 100);
INSERT INTO `attendance_records_score` VALUES (52, 20211203983, '郑久彤', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (109, 20211203986, '崔惟桓', '2021软件工程2班', 100, 0, 67, 85, 100);
INSERT INTO `attendance_records_score` VALUES (110, 20211203987, '刘晨阳', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (111, 20211203994, '吴航宇', '2021软件工程2班', 0, 0, 33, 100, 90);
INSERT INTO `attendance_records_score` VALUES (112, 20211203996, '夏单祁', '2021软件工程2班', 100, 100, 90, 90, 100);
INSERT INTO `attendance_records_score` VALUES (53, 20211204314, '阮龙', '2021软件工程1班', 100, 100, 100, 100, 90);
INSERT INTO `attendance_records_score` VALUES (54, 20211204412, '唐韧', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (55, 20211204414, '周作友', '2021软件工程1班', 100, 100, 100, 100, 90);
INSERT INTO `attendance_records_score` VALUES (113, 20211204434, '尹才华', '2021软件工程2班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (56, 20211204954, '张溪桐', '2021软件工程1班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (114, 20212200919, '何玉', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (149, 20212200937, '何紫萱', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (150, 20212200947, '梁雷', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (115, 20212200989, '袁晓淋', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (116, 20212201080, '曹祝群', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (117, 20212201098, '陈前', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (151, 20212201128, '吕茂奎', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (118, 20212201146, '杨承璐', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (119, 20212201172, '龚相涛', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (152, 20212201192, '杨大鹏', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (153, 20212201227, '李有英', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (120, 20212201251, '王志远', '2021软件工程3班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (121, 20212201258, '张玉钦', '2021软件工程3班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (122, 20212201310, '王藜璇', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (154, 20212201312, '蔡昊洋', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (155, 20212201313, '赵润萍', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (156, 20212201315, '王茂', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (123, 20212201320, '张涛', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (157, 20212201321, '李明坤', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (158, 20212201323, '廖雅杰', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (124, 20212201324, '郑俊', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (159, 20212201326, '张宇', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (125, 20212201330, '李正梅', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (160, 20212201331, '邓信松', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (126, 20212201335, '武丽', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (161, 20212201336, '欧阳进懿', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (162, 20212201340, '李天建', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (163, 20212201347, '刘沅超', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (127, 20212201350, '罗亚婷', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (128, 20212201351, '张文瑞', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (164, 20212201355, '王福禄', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (165, 20212201359, '张永丽', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (129, 20212201360, '邹洪东', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (130, 20212201365, '孟维', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (166, 20212201366, '陈应仙', '2021软件工程4班', 90, 90, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (167, 20212201367, '杨杨', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (168, 20212201369, '杨柠柠', '2021软件工程4班', 100, 100, 100, 100, 95);
INSERT INTO `attendance_records_score` VALUES (131, 20212201370, '施嘉鋆', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (132, 20212201373, '段周清', '2021软件工程3班', 100, 95, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (169, 20212201380, '亚比生', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (133, 20212201382, '段丽萍', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (170, 20212201385, '贾栋凯', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (134, 20212201391, '杨周成', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (171, 20212201392, '罗成亮', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (135, 20212201393, '张文腾', '2021软件工程3班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (172, 20212201394, '马露优', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (173, 20212201397, '王劲尧', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (136, 20212201399, '郑洁', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (174, 20212201400, '马明静', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (137, 20212201401, '徐艺', '2021软件工程3班', 100, 95, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (138, 20212201402, '伍吉红', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (139, 20212201403, '顾敬文', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (140, 20212201404, '吴水仙', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (175, 20212201405, '龚琛', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (141, 20212201408, '张运', '2021软件工程3班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (142, 20212201409, '姜人靖', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (176, 20212201410, '黄荣多', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (177, 20212201413, '李强贵', '2021软件工程4班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (178, 20212201414, '王晓敏', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (143, 20212201417, '陈寿富', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (179, 20212201420, '卢仕韦', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (144, 20212201423, '陈玉华', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (145, 20212201434, '龚礼东', '2021软件工程3班', 95, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (146, 20212201435, '杨宏发', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (147, 20212201436, '余晨', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (180, 20212201439, '赵昌粉', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (181, 20212201441, '茶炳榕', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (182, 20212201446, '余书艳', '2021软件工程4班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (148, 20212201448, '李瞵昌', '2021软件工程3班', 100, 100, 100, 100, 100);
INSERT INTO `attendance_records_score` VALUES (183, 20212201449, '张清远', '2021软件工程4班', 100, 100, 100, 100, 100);

-- ----------------------------
-- Table structure for experiment_reports_score
-- ----------------------------
DROP TABLE IF EXISTS `experiment_reports_score`;
CREATE TABLE `experiment_reports_score`  (
  `stu_number` int NULL DEFAULT NULL COMMENT '学生序号',
  `stu_id` bigint NOT NULL COMMENT '学生学号',
  `stu_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `stu_class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生班级',
  `one_score` double NULL DEFAULT NULL COMMENT '第一次成绩',
  `two_score` double NULL DEFAULT NULL COMMENT '第二次成绩',
  `three_sroce` double NULL DEFAULT NULL COMMENT '第三次成绩',
  `four_score` double NULL DEFAULT NULL COMMENT '第四次成绩',
  `five_score` double NULL DEFAULT NULL COMMENT '第五次成绩',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '实验报告分数表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of experiment_reports_score
-- ----------------------------
INSERT INTO `experiment_reports_score` VALUES (57, 20181203922, '王子康', '2021软件工程2班', 72, 78, 65, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (1, 20191202255, '纪嘉俊', '2021软件工程1班', 78, 77, 75, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (58, 20191202610, '段兴江', '2021软件工程2班', 77, 79, 77, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (2, 20201202139, '张子龙', '2021软件工程1班', 60, 76, 0, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (3, 20211200384, '严芊芊', '2021软件工程1班', 91, 78, 77, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (59, 20211200385, '顾培皓', '2021软件工程2班', 75, 71, 78, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (4, 20211200551, '曾繁一', '2021软件工程1班', 67, 74, 78, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (60, 20211200553, '王宗祥', '2021软件工程2班', 67, 82, 70, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (5, 20211200556, '王鑫', '2021软件工程1班', 85, 79, 70, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (6, 20211200558, '王贵萱', '2021软件工程1班', 78, 80, 86, 82, 0);
INSERT INTO `experiment_reports_score` VALUES (7, 20211200584, '何彦莹', '2021软件工程1班', 75, 82, 80, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (61, 20211200596, '于舒睿', '2021软件工程2班', 78, 75, 79, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (62, 20211200598, '张杨', '2021软件工程2班', 71, 70, 72, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (63, 20211200601, '孙欣欣', '2021软件工程2班', 92, 80, 78, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (8, 20211200602, '刘鑫宇', '2021软件工程1班', 60, 67, 62, 65, 0);
INSERT INTO `experiment_reports_score` VALUES (9, 20211200605, '郑琳', '2021软件工程1班', 89, 77, 74, 82, 0);
INSERT INTO `experiment_reports_score` VALUES (64, 20211200606, '迟稼铭', '2021软件工程2班', 77, 74, 65, 60, 0);
INSERT INTO `experiment_reports_score` VALUES (10, 20211200710, '汪康', '2021软件工程1班', 87, 0, 0, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (65, 20211200711, '章嘉劭', '2021软件工程2班', 72, 82, 76, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (11, 20211200719, '王鹏', '2021软件工程1班', 70, 82, 75, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (66, 20211201119, '王福龙', '2021软件工程2班', 78, 79, 71, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (12, 20211201141, '闫政', '2021软件工程1班', 86, 76, 83, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (13, 20211201148, '郭会发', '2021软件工程1班', 79, 76, 73, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (14, 20211201392, '孙可言', '2021软件工程1班', 78, 78, 71, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (15, 20211201418, '刘陵', '2021软件工程1班', 83, 81, 72, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (67, 20211201454, '何海兴', '2021软件工程2班', 75, 72, 74, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (68, 20211201457, '赵旋', '2021软件工程2班', 77, 67, 79, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (16, 20211201458, '焦海霞', '2021软件工程1班', 79, 84, 74, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (17, 20211201483, '张含锋', '2021软件工程1班', 78, 83, 81, 88, 0);
INSERT INTO `experiment_reports_score` VALUES (69, 20211201659, '彭锦龙', '2021软件工程2班', 76, 75, 66, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (70, 20211201766, '李欣欢', '2021软件工程2班', 78, 78, 76, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (71, 20211201785, '马乐晨', '2021软件工程2班', 61, 73, 74, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (72, 20211201793, '乔佳昕', '2021软件工程2班', 74, 80, 80, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (18, 20211201803, '张士博', '2021软件工程1班', 83, 71, 70, 63, 0);
INSERT INTO `experiment_reports_score` VALUES (19, 20211201804, '葛怀睿', '2021软件工程1班', 86, 70, 67, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (20, 20211201806, '刘帅博', '2021软件工程1班', 75, 67, 68, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (21, 20211201849, '魏继瑶', '2021软件工程1班', 67, 70, 71, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (73, 20211201867, '付陈瑶', '2021软件工程2班', 76, 75, 75, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (22, 20211201874, '郭伟康', '2021软件工程1班', 79, 77, 75, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (23, 20211201875, '王林超', '2021软件工程1班', 60, 0, 0, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (24, 20211201878, '杨嘉沐', '2021软件工程1班', 62, 83, 74, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (74, 20211201890, '常宏伟', '2021软件工程2班', 67, 80, 79, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (75, 20211201893, '韩森宇', '2021软件工程2班', 79, 69, 67, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (25, 20211201897, '张锐颀', '2021软件工程1班', 84, 67, 72, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (26, 20211201899, '刘子轩', '2021软件工程1班', 83, 66, 76, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (76, 20211201900, '王腾鑫', '2021软件工程2班', 78, 76, 80, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (77, 20211201902, '张睿泽', '2021软件工程2班', 70, 72, 74, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (27, 20211201903, '董美娇', '2021软件工程1班', 82, 81, 81, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (28, 20211202068, '常松', '2021软件工程1班', 83, 81, 75, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (78, 20211202069, '刘庆龙', '2021软件工程2班', 70, 64, 66, 61, 0);
INSERT INTO `experiment_reports_score` VALUES (79, 20211202072, '邢子阳', '2021软件工程2班', 76, 75, 77, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (29, 20211202073, '陈浩然', '2021软件工程1班', 76, 72, 81, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (80, 20211202079, '祁明扬', '2021软件工程2班', 86, 75, 67, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (81, 20211202081, '任靓', '2021软件工程2班', 73, 72, 76, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (30, 20211202083, '高铎', '2021软件工程1班', 76, 60, 65, 67, 0);
INSERT INTO `experiment_reports_score` VALUES (82, 20211202090, '姚祥桐', '2021软件工程2班', 74, 70, 78, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (83, 20211202095, '王雅鑫', '2021软件工程2班', 89, 71, 81, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (31, 20211202101, '陈广硕', '2021软件工程1班', 68, 71, 72, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (32, 20211202103, '张瑛琪', '2021软件工程1班', 79, 77, 79, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (84, 20211202104, '耿唯瀚', '2021软件工程2班', 67, 74, 74, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (33, 20211202111, '张博', '2021软件工程1班', 74, 68, 74, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (85, 20211202112, '李明哲', '2021软件工程2班', 76, 0, 77, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (34, 20211202125, '黄照凯', '2021软件工程1班', 79, 71, 0, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (86, 20211202312, '徐婷', '2021软件工程2班', 86, 74, 75, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (35, 20211202326, '李俊兰', '2021软件工程1班', 77, 79, 81, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (87, 20211202355, '支毅博', '2021软件工程2班', 72, 76, 76, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (88, 20211202362, '赵佳乐', '2021软件工程2班', 81, 72, 0, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (36, 20211202380, '李轩', '2021软件工程1班', 72, 85, 78, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (89, 20211202487, '翟翱', '2021软件工程2班', 67, 74, 70, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (37, 20211202495, '饶峰', '2021软件工程1班', 86, 73, 76, 63, 0);
INSERT INTO `experiment_reports_score` VALUES (38, 20211202543, '罗民富', '2021软件工程1班', 77, 75, 75, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (39, 20211202705, '丁金洋', '2021软件工程1班', 74, 72, 75, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (90, 20211202720, '张书通', '2021软件工程2班', 82, 72, 75, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (40, 20211202723, '田兆卓', '2021软件工程1班', 82, 84, 83, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (41, 20211202724, '王洪福', '2021软件工程1班', 70, 76, 74, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (91, 20211202726, '李韩', '2021软件工程2班', 71, 70, 73, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (92, 20211202730, '郭桐羽', '2021软件工程2班', 75, 76, 75, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (93, 20211202732, '张宇', '2021软件工程2班', 69, 75, 75, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (94, 20211202744, '王祉桥', '2021软件工程2班', 70, 71, 73, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (95, 20211202754, '刘扬', '2021软件工程2班', 67, 77, 72, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (42, 20211202759, '唐文勃', '2021软件工程1班', 60, 64, 0, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (96, 20211202822, '何通海', '2021软件工程2班', 76, 76, 76, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (97, 20211202855, '任子豪', '2021软件工程2班', 82, 75, 69, 69, 0);
INSERT INTO `experiment_reports_score` VALUES (43, 20211202868, '孙艺慧', '2021软件工程1班', 78, 78, 82, 82, 0);
INSERT INTO `experiment_reports_score` VALUES (44, 20211202878, '涂泉源', '2021软件工程1班', 73, 81, 83, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (98, 20211202881, '吴健南', '2021软件工程2班', 72, 78, 68, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (45, 20211202900, '陈梦飞', '2021软件工程1班', 72, 81, 83, 83, 0);
INSERT INTO `experiment_reports_score` VALUES (99, 20211202947, '许孙凯', '2021软件工程2班', 85, 78, 72, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (100, 20211202948, '白明涛', '2021软件工程2班', 81, 71, 71, 83, 0);
INSERT INTO `experiment_reports_score` VALUES (46, 20211203012, '王冠涵', '2021软件工程1班', 86, 78, 71, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (47, 20211203035, '卢平', '2021软件工程1班', 82, 67, 70, 73, 0);
INSERT INTO `experiment_reports_score` VALUES (48, 20211203038, '刘浩宇', '2021软件工程1班', 73, 75, 72, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (101, 20211203042, '信帅权', '2021软件工程2班', 75, 76, 75, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (102, 20211203047, '邓大卫', '2021软件工程2班', 81, 75, 72, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (49, 20211203049, '尹春普', '2021软件工程1班', 63, 86, 75, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (103, 20211203059, '刘思豪', '2021软件工程2班', 87, 75, 73, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (104, 20211203089, '张义超', '2021软件工程2班', 74, 75, 0, 67, 0);
INSERT INTO `experiment_reports_score` VALUES (105, 20211203091, '王格格', '2021软件工程2班', 75, 79, 82, 68, 0);
INSERT INTO `experiment_reports_score` VALUES (50, 20211203783, '张楠', '2021软件工程1班', 86, 76, 70, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (106, 20211203792, '戴明东', '2021软件工程2班', 75, 81, 84, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (107, 20211203974, '李涵', '2021软件工程2班', 71, 73, 75, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (108, 20211203978, '栾凯越', '2021软件工程2班', 86, 79, 80, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (51, 20211203980, '刘佳欣', '2021软件工程1班', 85, 76, 75, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (52, 20211203983, '郑久彤', '2021软件工程1班', 75, 82, 83, 83, 0);
INSERT INTO `experiment_reports_score` VALUES (109, 20211203986, '崔惟桓', '2021软件工程2班', 64, 68, 64, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (110, 20211203987, '刘晨阳', '2021软件工程2班', 76, 72, 78, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (111, 20211203994, '吴航宇', '2021软件工程2班', 64, 74, 61, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (112, 20211203996, '夏单祁', '2021软件工程2班', 73, 63, 61, 65, 0);
INSERT INTO `experiment_reports_score` VALUES (53, 20211204314, '阮龙', '2021软件工程1班', 72, 77, 0, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (54, 20211204412, '唐韧', '2021软件工程1班', 76, 86, 70, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (55, 20211204414, '周作友', '2021软件工程1班', 79, 76, 75, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (113, 20211204434, '尹才华', '2021软件工程2班', 75, 68, 70, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (56, 20211204954, '张溪桐', '2021软件工程1班', 78, 78, 70, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (114, 20212200919, '何玉', '2021软件工程3班', 80, 78, 76, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (149, 20212200937, '何紫萱', '2021软件工程4班', 82, 88, 89, 84, 0);
INSERT INTO `experiment_reports_score` VALUES (150, 20212200947, '梁雷', '2021软件工程4班', 95, 72, 74, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (115, 20212200989, '袁晓淋', '2021软件工程3班', 70, 76, 72, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (116, 20212201080, '曹祝群', '2021软件工程3班', 71, 70, 89, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (117, 20212201098, '陈前', '2021软件工程3班', 79, 75, 76, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (151, 20212201128, '吕茂奎', '2021软件工程4班', 75, 78, 80, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (118, 20212201146, '杨承璐', '2021软件工程3班', 96, 70, 79, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (119, 20212201172, '龚相涛', '2021软件工程3班', 75, 78, 77, 89, 0);
INSERT INTO `experiment_reports_score` VALUES (152, 20212201192, '杨大鹏', '2021软件工程4班', 78, 82, 79, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (153, 20212201227, '李有英', '2021软件工程4班', 68, 82, 78, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (120, 20212201251, '王志远', '2021软件工程3班', 79, 79, 73, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (121, 20212201258, '张玉钦', '2021软件工程3班', 75, 76, 78, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (122, 20212201310, '王藜璇', '2021软件工程3班', 75, 76, 79, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (154, 20212201312, '蔡昊洋', '2021软件工程4班', 79, 81, 78, 64, 0);
INSERT INTO `experiment_reports_score` VALUES (155, 20212201313, '赵润萍', '2021软件工程4班', 100, 82, 88, 84, 0);
INSERT INTO `experiment_reports_score` VALUES (156, 20212201315, '王茂', '2021软件工程4班', 78, 75, 82, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (123, 20212201320, '张涛', '2021软件工程3班', 72, 72, 75, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (157, 20212201321, '李明坤', '2021软件工程4班', 76, 83, 75, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (158, 20212201323, '廖雅杰', '2021软件工程4班', 92, 75, 78, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (124, 20212201324, '郑俊', '2021软件工程3班', 76, 73, 79, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (159, 20212201326, '张宇', '2021软件工程4班', 83, 72, 71, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (125, 20212201330, '李正梅', '2021软件工程3班', 72, 70, 74, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (160, 20212201331, '邓信松', '2021软件工程4班', 84, 83, 82, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (126, 20212201335, '武丽', '2021软件工程3班', 85, 73, 75, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (161, 20212201336, '欧阳进懿', '2021软件工程4班', 100, 75, 82, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (162, 20212201340, '李天建', '2021软件工程4班', 100, 75, 90, 88, 0);
INSERT INTO `experiment_reports_score` VALUES (163, 20212201347, '刘沅超', '2021软件工程4班', 86, 74, 83, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (127, 20212201350, '罗亚婷', '2021软件工程3班', 72, 75, 81, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (128, 20212201351, '张文瑞', '2021软件工程3班', 76, 77, 70, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (164, 20212201355, '王福禄', '2021软件工程4班', 77, 71, 76, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (165, 20212201359, '张永丽', '2021软件工程4班', 75, 82, 81, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (129, 20212201360, '邹洪东', '2021软件工程3班', 78, 83, 83, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (130, 20212201365, '孟维', '2021软件工程3班', 72, 75, 75, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (166, 20212201366, '陈应仙', '2021软件工程4班', 86, 94, 77, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (167, 20212201367, '杨杨', '2021软件工程4班', 100, 79, 74, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (168, 20212201369, '杨柠柠', '2021软件工程4班', 88, 0, 81, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (131, 20212201370, '施嘉鋆', '2021软件工程3班', 82, 77, 72, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (132, 20212201373, '段周清', '2021软件工程3班', 75, 81, 84, 0, 0);
INSERT INTO `experiment_reports_score` VALUES (169, 20212201380, '亚比生', '2021软件工程4班', 74, 80, 75, 69, 0);
INSERT INTO `experiment_reports_score` VALUES (133, 20212201382, '段丽萍', '2021软件工程3班', 82, 89, 94, 83, 0);
INSERT INTO `experiment_reports_score` VALUES (170, 20212201385, '贾栋凯', '2021软件工程4班', 73, 76, 83, 69, 0);
INSERT INTO `experiment_reports_score` VALUES (134, 20212201391, '杨周成', '2021软件工程3班', 64, 71, 76, 81, 0);
INSERT INTO `experiment_reports_score` VALUES (171, 20212201392, '罗成亮', '2021软件工程4班', 87, 89, 78, 85, 0);
INSERT INTO `experiment_reports_score` VALUES (135, 20212201393, '张文腾', '2021软件工程3班', 87, 77, 74, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (172, 20212201394, '马露优', '2021软件工程4班', 75, 83, 83, 82, 0);
INSERT INTO `experiment_reports_score` VALUES (173, 20212201397, '王劲尧', '2021软件工程4班', 91, 71, 72, 74, 0);
INSERT INTO `experiment_reports_score` VALUES (136, 20212201399, '郑洁', '2021软件工程3班', 78, 75, 75, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (174, 20212201400, '马明静', '2021软件工程4班', 76, 81, 77, 86, 0);
INSERT INTO `experiment_reports_score` VALUES (137, 20212201401, '徐艺', '2021软件工程3班', 85, 80, 79, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (138, 20212201402, '伍吉红', '2021软件工程3班', 73, 79, 82, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (139, 20212201403, '顾敬文', '2021软件工程3班', 77, 73, 83, 78, 0);
INSERT INTO `experiment_reports_score` VALUES (140, 20212201404, '吴水仙', '2021软件工程3班', 81, 75, 78, 69, 0);
INSERT INTO `experiment_reports_score` VALUES (175, 20212201405, '龚琛', '2021软件工程4班', 69, 81, 71, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (141, 20212201408, '张运', '2021软件工程3班', 81, 72, 78, 69, 0);
INSERT INTO `experiment_reports_score` VALUES (142, 20212201409, '姜人靖', '2021软件工程3班', 73, 76, 75, 82, 0);
INSERT INTO `experiment_reports_score` VALUES (176, 20212201410, '黄荣多', '2021软件工程4班', 94, 72, 77, 76, 0);
INSERT INTO `experiment_reports_score` VALUES (177, 20212201413, '李强贵', '2021软件工程4班', 100, 75, 80, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (178, 20212201414, '王晓敏', '2021软件工程4班', 92, 79, 78, 79, 0);
INSERT INTO `experiment_reports_score` VALUES (143, 20212201417, '陈寿富', '2021软件工程3班', 70, 74, 72, 72, 0);
INSERT INTO `experiment_reports_score` VALUES (179, 20212201420, '卢仕韦', '2021软件工程4班', 95, 79, 85, 80, 0);
INSERT INTO `experiment_reports_score` VALUES (144, 20212201423, '陈玉华', '2021软件工程3班', 76, 75, 79, 71, 0);
INSERT INTO `experiment_reports_score` VALUES (145, 20212201434, '龚礼东', '2021软件工程3班', 71, 86, 87, 83, 0);
INSERT INTO `experiment_reports_score` VALUES (146, 20212201435, '杨宏发', '2021软件工程3班', 74, 76, 79, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (147, 20212201436, '余晨', '2021软件工程3班', 75, 77, 78, 70, 0);
INSERT INTO `experiment_reports_score` VALUES (180, 20212201439, '赵昌粉', '2021软件工程4班', 83, 88, 85, 75, 0);
INSERT INTO `experiment_reports_score` VALUES (181, 20212201441, '茶炳榕', '2021软件工程4班', 83, 76, 78, 67, 0);
INSERT INTO `experiment_reports_score` VALUES (182, 20212201446, '余书艳', '2021软件工程4班', 100, 92, 86, 77, 0);
INSERT INTO `experiment_reports_score` VALUES (148, 20212201448, '李瞵昌', '2021软件工程3班', 74, 70, 82, 65, 0);
INSERT INTO `experiment_reports_score` VALUES (183, 20212201449, '张清远', '2021软件工程4班', 25, 70, 79, 77, 0);

-- ----------------------------
-- Table structure for final_visit_score
-- ----------------------------
DROP TABLE IF EXISTS `final_visit_score`;
CREATE TABLE `final_visit_score`  (
  `stu_number` int NULL DEFAULT NULL COMMENT '学生序号',
  `stu_id` bigint NOT NULL COMMENT '学生学号',
  `stu_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `stu_class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生班级',
  `score` double NULL DEFAULT NULL COMMENT '期末成绩',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '期末考察分数表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of final_visit_score
-- ----------------------------
INSERT INTO `final_visit_score` VALUES (57, 20181203922, '王子康', '2021软件工程2班', 74);
INSERT INTO `final_visit_score` VALUES (1, 20191202255, '纪嘉俊', '2021软件工程1班', 81);
INSERT INTO `final_visit_score` VALUES (58, 20191202610, '段兴江', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (2, 20201202139, '张子龙', '2021软件工程1班', 0);
INSERT INTO `final_visit_score` VALUES (3, 20211200384, '严芊芊', '2021软件工程1班', 91);
INSERT INTO `final_visit_score` VALUES (59, 20211200385, '顾培皓', '2021软件工程2班', 83);
INSERT INTO `final_visit_score` VALUES (4, 20211200551, '曾繁一', '2021软件工程1班', 82);
INSERT INTO `final_visit_score` VALUES (60, 20211200553, '王宗祥', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (5, 20211200556, '王鑫', '2021软件工程1班', 78);
INSERT INTO `final_visit_score` VALUES (6, 20211200558, '王贵萱', '2021软件工程1班', 93);
INSERT INTO `final_visit_score` VALUES (7, 20211200584, '何彦莹', '2021软件工程1班', 92);
INSERT INTO `final_visit_score` VALUES (61, 20211200596, '于舒睿', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (62, 20211200598, '张杨', '2021软件工程2班', 88);
INSERT INTO `final_visit_score` VALUES (63, 20211200601, '孙欣欣', '2021软件工程2班', 86);
INSERT INTO `final_visit_score` VALUES (8, 20211200602, '刘鑫宇', '2021软件工程1班', 60);
INSERT INTO `final_visit_score` VALUES (9, 20211200605, '郑琳', '2021软件工程1班', 86);
INSERT INTO `final_visit_score` VALUES (64, 20211200606, '迟稼铭', '2021软件工程2班', 72);
INSERT INTO `final_visit_score` VALUES (10, 20211200710, '汪康', '2021软件工程1班', 73);
INSERT INTO `final_visit_score` VALUES (65, 20211200711, '章嘉劭', '2021软件工程2班', 75);
INSERT INTO `final_visit_score` VALUES (11, 20211200719, '王鹏', '2021软件工程1班', 81);
INSERT INTO `final_visit_score` VALUES (66, 20211201119, '王福龙', '2021软件工程2班', 78);
INSERT INTO `final_visit_score` VALUES (12, 20211201141, '闫政', '2021软件工程1班', 83);
INSERT INTO `final_visit_score` VALUES (13, 20211201148, '郭会发', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (14, 20211201392, '孙可言', '2021软件工程1班', 73);
INSERT INTO `final_visit_score` VALUES (15, 20211201418, '刘陵', '2021软件工程1班', 71);
INSERT INTO `final_visit_score` VALUES (67, 20211201454, '何海兴', '2021软件工程2班', 86);
INSERT INTO `final_visit_score` VALUES (68, 20211201457, '赵旋', '2021软件工程2班', 74);
INSERT INTO `final_visit_score` VALUES (16, 20211201458, '焦海霞', '2021软件工程1班', 93);
INSERT INTO `final_visit_score` VALUES (17, 20211201483, '张含锋', '2021软件工程1班', 93);
INSERT INTO `final_visit_score` VALUES (69, 20211201659, '彭锦龙', '2021软件工程2班', 77);
INSERT INTO `final_visit_score` VALUES (70, 20211201766, '李欣欢', '2021软件工程2班', 89);
INSERT INTO `final_visit_score` VALUES (71, 20211201785, '马乐晨', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (72, 20211201793, '乔佳昕', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (18, 20211201803, '张士博', '2021软件工程1班', 71);
INSERT INTO `final_visit_score` VALUES (19, 20211201804, '葛怀睿', '2021软件工程1班', 80);
INSERT INTO `final_visit_score` VALUES (20, 20211201806, '刘帅博', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (21, 20211201849, '魏继瑶', '2021软件工程1班', 78);
INSERT INTO `final_visit_score` VALUES (73, 20211201867, '付陈瑶', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (22, 20211201874, '郭伟康', '2021软件工程1班', 80);
INSERT INTO `final_visit_score` VALUES (23, 20211201875, '王林超', '2021软件工程1班', 0);
INSERT INTO `final_visit_score` VALUES (24, 20211201878, '杨嘉沐', '2021软件工程1班', 87);
INSERT INTO `final_visit_score` VALUES (74, 20211201890, '常宏伟', '2021软件工程2班', 83);
INSERT INTO `final_visit_score` VALUES (75, 20211201893, '韩森宇', '2021软件工程2班', 70);
INSERT INTO `final_visit_score` VALUES (25, 20211201897, '张锐颀', '2021软件工程1班', 89);
INSERT INTO `final_visit_score` VALUES (26, 20211201899, '刘子轩', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (76, 20211201900, '王腾鑫', '2021软件工程2班', 84);
INSERT INTO `final_visit_score` VALUES (77, 20211201902, '张睿泽', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (27, 20211201903, '董美娇', '2021软件工程1班', 78);
INSERT INTO `final_visit_score` VALUES (28, 20211202068, '常松', '2021软件工程1班', 82);
INSERT INTO `final_visit_score` VALUES (78, 20211202069, '刘庆龙', '2021软件工程2班', 65);
INSERT INTO `final_visit_score` VALUES (79, 20211202072, '邢子阳', '2021软件工程2班', 77);
INSERT INTO `final_visit_score` VALUES (29, 20211202073, '陈浩然', '2021软件工程1班', 78);
INSERT INTO `final_visit_score` VALUES (80, 20211202079, '祁明扬', '2021软件工程2班', 88);
INSERT INTO `final_visit_score` VALUES (81, 20211202081, '任靓', '2021软件工程2班', 76);
INSERT INTO `final_visit_score` VALUES (30, 20211202083, '高铎', '2021软件工程1班', 60);
INSERT INTO `final_visit_score` VALUES (82, 20211202090, '姚祥桐', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (83, 20211202095, '王雅鑫', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (31, 20211202101, '陈广硕', '2021软件工程1班', 81);
INSERT INTO `final_visit_score` VALUES (32, 20211202103, '张瑛琪', '2021软件工程1班', 84);
INSERT INTO `final_visit_score` VALUES (84, 20211202104, '耿唯瀚', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (33, 20211202111, '张博', '2021软件工程1班', 79);
INSERT INTO `final_visit_score` VALUES (85, 20211202112, '李明哲', '2021软件工程2班', 75);
INSERT INTO `final_visit_score` VALUES (34, 20211202125, '黄照凯', '2021软件工程1班', 63);
INSERT INTO `final_visit_score` VALUES (86, 20211202312, '徐婷', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (35, 20211202326, '李俊兰', '2021软件工程1班', 90);
INSERT INTO `final_visit_score` VALUES (87, 20211202355, '支毅博', '2021软件工程2班', 77);
INSERT INTO `final_visit_score` VALUES (88, 20211202362, '赵佳乐', '2021软件工程2班', 86);
INSERT INTO `final_visit_score` VALUES (36, 20211202380, '李轩', '2021软件工程1班', 81);
INSERT INTO `final_visit_score` VALUES (89, 20211202487, '翟翱', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (37, 20211202495, '饶峰', '2021软件工程1班', 83);
INSERT INTO `final_visit_score` VALUES (38, 20211202543, '罗民富', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (39, 20211202705, '丁金洋', '2021软件工程1班', 86);
INSERT INTO `final_visit_score` VALUES (90, 20211202720, '张书通', '2021软件工程2班', 72);
INSERT INTO `final_visit_score` VALUES (40, 20211202723, '田兆卓', '2021软件工程1班', 88);
INSERT INTO `final_visit_score` VALUES (41, 20211202724, '王洪福', '2021软件工程1班', 76);
INSERT INTO `final_visit_score` VALUES (91, 20211202726, '李韩', '2021软件工程2班', 87);
INSERT INTO `final_visit_score` VALUES (92, 20211202730, '郭桐羽', '2021软件工程2班', 78);
INSERT INTO `final_visit_score` VALUES (93, 20211202732, '张宇', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (94, 20211202744, '王祉桥', '2021软件工程2班', 86);
INSERT INTO `final_visit_score` VALUES (95, 20211202754, '刘扬', '2021软件工程2班', 80);
INSERT INTO `final_visit_score` VALUES (42, 20211202759, '唐文勃', '2021软件工程1班', 77);
INSERT INTO `final_visit_score` VALUES (96, 20211202822, '何通海', '2021软件工程2班', 85);
INSERT INTO `final_visit_score` VALUES (97, 20211202855, '任子豪', '2021软件工程2班', 82);
INSERT INTO `final_visit_score` VALUES (43, 20211202868, '孙艺慧', '2021软件工程1班', 94);
INSERT INTO `final_visit_score` VALUES (44, 20211202878, '涂泉源', '2021软件工程1班', 89);
INSERT INTO `final_visit_score` VALUES (98, 20211202881, '吴健南', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (45, 20211202900, '陈梦飞', '2021软件工程1班', 88);
INSERT INTO `final_visit_score` VALUES (99, 20211202947, '许孙凯', '2021软件工程2班', 75);
INSERT INTO `final_visit_score` VALUES (100, 20211202948, '白明涛', '2021软件工程2班', 72);
INSERT INTO `final_visit_score` VALUES (46, 20211203012, '王冠涵', '2021软件工程1班', 80);
INSERT INTO `final_visit_score` VALUES (47, 20211203035, '卢平', '2021软件工程1班', 65);
INSERT INTO `final_visit_score` VALUES (48, 20211203038, '刘浩宇', '2021软件工程1班', 78);
INSERT INTO `final_visit_score` VALUES (101, 20211203042, '信帅权', '2021软件工程2班', 0);
INSERT INTO `final_visit_score` VALUES (102, 20211203047, '邓大卫', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (49, 20211203049, '尹春普', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (103, 20211203059, '刘思豪', '2021软件工程2班', 87);
INSERT INTO `final_visit_score` VALUES (104, 20211203089, '张义超', '2021软件工程2班', 67);
INSERT INTO `final_visit_score` VALUES (105, 20211203091, '王格格', '2021软件工程2班', 83);
INSERT INTO `final_visit_score` VALUES (50, 20211203783, '张楠', '2021软件工程1班', 83);
INSERT INTO `final_visit_score` VALUES (106, 20211203792, '戴明东', '2021软件工程2班', 81);
INSERT INTO `final_visit_score` VALUES (107, 20211203974, '李涵', '2021软件工程2班', 77);
INSERT INTO `final_visit_score` VALUES (108, 20211203978, '栾凯越', '2021软件工程2班', 83);
INSERT INTO `final_visit_score` VALUES (51, 20211203980, '刘佳欣', '2021软件工程1班', 79);
INSERT INTO `final_visit_score` VALUES (52, 20211203983, '郑久彤', '2021软件工程1班', 88);
INSERT INTO `final_visit_score` VALUES (109, 20211203986, '崔惟桓', '2021软件工程2班', 0);
INSERT INTO `final_visit_score` VALUES (110, 20211203987, '刘晨阳', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (111, 20211203994, '吴航宇', '2021软件工程2班', 70);
INSERT INTO `final_visit_score` VALUES (112, 20211203996, '夏单祁', '2021软件工程2班', 74);
INSERT INTO `final_visit_score` VALUES (53, 20211204314, '阮龙', '2021软件工程1班', 79);
INSERT INTO `final_visit_score` VALUES (54, 20211204412, '唐韧', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (55, 20211204414, '周作友', '2021软件工程1班', 85);
INSERT INTO `final_visit_score` VALUES (113, 20211204434, '尹才华', '2021软件工程2班', 79);
INSERT INTO `final_visit_score` VALUES (56, 20211204954, '张溪桐', '2021软件工程1班', 82);
INSERT INTO `final_visit_score` VALUES (114, 20212200919, '何玉', '2021软件工程3班', 79);
INSERT INTO `final_visit_score` VALUES (149, 20212200937, '何紫萱', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (150, 20212200947, '梁雷', '2021软件工程4班', 83);
INSERT INTO `final_visit_score` VALUES (115, 20212200989, '袁晓淋', '2021软件工程3班', 87);
INSERT INTO `final_visit_score` VALUES (116, 20212201080, '曹祝群', '2021软件工程3班', 92);
INSERT INTO `final_visit_score` VALUES (117, 20212201098, '陈前', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (151, 20212201128, '吕茂奎', '2021软件工程4班', 81);
INSERT INTO `final_visit_score` VALUES (118, 20212201146, '杨承璐', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (119, 20212201172, '龚相涛', '2021软件工程3班', 82);
INSERT INTO `final_visit_score` VALUES (152, 20212201192, '杨大鹏', '2021软件工程4班', 81);
INSERT INTO `final_visit_score` VALUES (153, 20212201227, '李有英', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (120, 20212201251, '王志远', '2021软件工程3班', 82);
INSERT INTO `final_visit_score` VALUES (121, 20212201258, '张玉钦', '2021软件工程3班', 81);
INSERT INTO `final_visit_score` VALUES (122, 20212201310, '王藜璇', '2021软件工程3班', 80);
INSERT INTO `final_visit_score` VALUES (154, 20212201312, '蔡昊洋', '2021软件工程4班', 76);
INSERT INTO `final_visit_score` VALUES (155, 20212201313, '赵润萍', '2021软件工程4班', 93);
INSERT INTO `final_visit_score` VALUES (156, 20212201315, '王茂', '2021软件工程4班', 88);
INSERT INTO `final_visit_score` VALUES (123, 20212201320, '张涛', '2021软件工程3班', 75);
INSERT INTO `final_visit_score` VALUES (157, 20212201321, '李明坤', '2021软件工程4班', 79);
INSERT INTO `final_visit_score` VALUES (158, 20212201323, '廖雅杰', '2021软件工程4班', 78);
INSERT INTO `final_visit_score` VALUES (124, 20212201324, '郑俊', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (159, 20212201326, '张宇', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (125, 20212201330, '李正梅', '2021软件工程3班', 82);
INSERT INTO `final_visit_score` VALUES (160, 20212201331, '邓信松', '2021软件工程4班', 91);
INSERT INTO `final_visit_score` VALUES (126, 20212201335, '武丽', '2021软件工程3班', 90);
INSERT INTO `final_visit_score` VALUES (161, 20212201336, '欧阳进懿', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (162, 20212201340, '李天建', '2021软件工程4班', 92);
INSERT INTO `final_visit_score` VALUES (163, 20212201347, '刘沅超', '2021软件工程4班', 82);
INSERT INTO `final_visit_score` VALUES (127, 20212201350, '罗亚婷', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (128, 20212201351, '张文瑞', '2021软件工程3班', 85);
INSERT INTO `final_visit_score` VALUES (164, 20212201355, '王福禄', '2021软件工程4班', 81);
INSERT INTO `final_visit_score` VALUES (165, 20212201359, '张永丽', '2021软件工程4班', 93);
INSERT INTO `final_visit_score` VALUES (129, 20212201360, '邹洪东', '2021软件工程3班', 84);
INSERT INTO `final_visit_score` VALUES (130, 20212201365, '孟维', '2021软件工程3班', 81);
INSERT INTO `final_visit_score` VALUES (166, 20212201366, '陈应仙', '2021软件工程4班', 90);
INSERT INTO `final_visit_score` VALUES (167, 20212201367, '杨杨', '2021软件工程4班', 88);
INSERT INTO `final_visit_score` VALUES (168, 20212201369, '杨柠柠', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (131, 20212201370, '施嘉鋆', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (132, 20212201373, '段周清', '2021软件工程3班', 84);
INSERT INTO `final_visit_score` VALUES (169, 20212201380, '亚比生', '2021软件工程4班', 88);
INSERT INTO `final_visit_score` VALUES (133, 20212201382, '段丽萍', '2021软件工程3班', 72);
INSERT INTO `final_visit_score` VALUES (170, 20212201385, '贾栋凯', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (134, 20212201391, '杨周成', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (171, 20212201392, '罗成亮', '2021软件工程4班', 93);
INSERT INTO `final_visit_score` VALUES (135, 20212201393, '张文腾', '2021软件工程3班', 81);
INSERT INTO `final_visit_score` VALUES (172, 20212201394, '马露优', '2021软件工程4班', 89);
INSERT INTO `final_visit_score` VALUES (173, 20212201397, '王劲尧', '2021软件工程4班', 76);
INSERT INTO `final_visit_score` VALUES (136, 20212201399, '郑洁', '2021软件工程3班', 85);
INSERT INTO `final_visit_score` VALUES (174, 20212201400, '马明静', '2021软件工程4班', 86);
INSERT INTO `final_visit_score` VALUES (137, 20212201401, '徐艺', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (138, 20212201402, '伍吉红', '2021软件工程3班', 82);
INSERT INTO `final_visit_score` VALUES (139, 20212201403, '顾敬文', '2021软件工程3班', 81);
INSERT INTO `final_visit_score` VALUES (140, 20212201404, '吴水仙', '2021软件工程3班', 82);
INSERT INTO `final_visit_score` VALUES (175, 20212201405, '龚琛', '2021软件工程4班', 78);
INSERT INTO `final_visit_score` VALUES (141, 20212201408, '张运', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (142, 20212201409, '姜人靖', '2021软件工程3班', 86);
INSERT INTO `final_visit_score` VALUES (176, 20212201410, '黄荣多', '2021软件工程4班', 85);
INSERT INTO `final_visit_score` VALUES (177, 20212201413, '李强贵', '2021软件工程4班', 81);
INSERT INTO `final_visit_score` VALUES (178, 20212201414, '王晓敏', '2021软件工程4班', 84);
INSERT INTO `final_visit_score` VALUES (143, 20212201417, '陈寿富', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (179, 20212201420, '卢仕韦', '2021软件工程4班', 84);
INSERT INTO `final_visit_score` VALUES (144, 20212201423, '陈玉华', '2021软件工程3班', 81);
INSERT INTO `final_visit_score` VALUES (145, 20212201434, '龚礼东', '2021软件工程3班', 89);
INSERT INTO `final_visit_score` VALUES (146, 20212201435, '杨宏发', '2021软件工程3班', 76);
INSERT INTO `final_visit_score` VALUES (147, 20212201436, '余晨', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (180, 20212201439, '赵昌粉', '2021软件工程4班', 89);
INSERT INTO `final_visit_score` VALUES (181, 20212201441, '茶炳榕', '2021软件工程4班', 86);
INSERT INTO `final_visit_score` VALUES (182, 20212201446, '余书艳', '2021软件工程4班', 88);
INSERT INTO `final_visit_score` VALUES (148, 20212201448, '李瞵昌', '2021软件工程3班', 83);
INSERT INTO `final_visit_score` VALUES (183, 20212201449, '张清远', '2021软件工程4班', 90);

-- ----------------------------
-- Table structure for hui_hui
-- ----------------------------
DROP TABLE IF EXISTS `hui_hui`;
CREATE TABLE `hui_hui`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `hi` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hui_hui
-- ----------------------------
INSERT INTO `hui_hui` VALUES (1, '2', '3');
INSERT INTO `hui_hui` VALUES (2, '3', '4');
INSERT INTO `hui_hui` VALUES (3, 'huihui', 'demo');

-- ----------------------------
-- Table structure for lishihui_system_user
-- ----------------------------
DROP TABLE IF EXISTS `lishihui_system_user`;
CREATE TABLE `lishihui_system_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` int NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birthday` date NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `delstatus` int NULL DEFAULT 0,
  `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime NULL DEFAULT NULL COMMENT '修改时间',
  `version` int NULL DEFAULT 1 COMMENT '乐观锁',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 74 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '逻辑删去-默认是0，逻辑删去后标为1' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lishihui_system_user
-- ----------------------------
INSERT INTO `lishihui_system_user` VALUES (2, '张俊杰', '123', '男', 12, '15812341234', '中国', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (24, '花猫', '123', '男', 29, '17687188085', '丽江', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (26, '天蓬', '999999', '1111', 50, '1111', '111', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (29, '1111', NULL, 'nan', 18, '', 'xx', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (30, 'ka', NULL, '1', 15, '2456', '3', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (32, 'admins', NULL, '女', 18, '12', '硅谷', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (33, '宝玉', '123456', '男', 22, '4521', NULL, NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (35, '', NULL, '666', 26, '', '', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (37, '', NULL, '女', 18, '', '沈阳大街', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (38, '日光', NULL, '男', 21, '', '地球核心', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (66, '小歪', NULL, '女', 21, '', '月球', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (67, '小花猫', '333', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (68, '大花猫', NULL, '男', 19, '123', '123', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (70, '1', NULL, '女', 78, '44058871', '丽江', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (72, 't', '123', NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (73, '123', NULL, '789', 456, '123', '789', NULL, NULL, 0, NULL, NULL, 1);

-- ----------------------------
-- Table structure for project_checks_score
-- ----------------------------
DROP TABLE IF EXISTS `project_checks_score`;
CREATE TABLE `project_checks_score`  (
  `stu_number` int NULL DEFAULT NULL COMMENT '学生序号',
  `stu_id` bigint NOT NULL COMMENT '学生学号',
  `stu_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `stu_class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生班级',
  `one_score` double NULL DEFAULT NULL COMMENT '第一次成绩',
  `two_score` double NULL DEFAULT NULL COMMENT '第二次成绩',
  `three_sroce` double NULL DEFAULT NULL COMMENT '第三次成绩',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '项目检查分数表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project_checks_score
-- ----------------------------
INSERT INTO `project_checks_score` VALUES (57, 20181203922, '王子康', '2021软件工程2班', 60, 0, 100);
INSERT INTO `project_checks_score` VALUES (1, 20191202255, '纪嘉俊', '2021软件工程1班', 95, 0, 100);
INSERT INTO `project_checks_score` VALUES (58, 20191202610, '段兴江', '2021软件工程2班', 90, -10, 100);
INSERT INTO `project_checks_score` VALUES (2, 20201202139, '张子龙', '2021软件工程1班', 0, 0, 0);
INSERT INTO `project_checks_score` VALUES (3, 20211200384, '严芊芊', '2021软件工程1班', 100, 100, 100);
INSERT INTO `project_checks_score` VALUES (59, 20211200385, '顾培皓', '2021软件工程2班', 75, -40, 100);
INSERT INTO `project_checks_score` VALUES (4, 20211200551, '曾繁一', '2021软件工程1班', 98, 80, 100);
INSERT INTO `project_checks_score` VALUES (60, 20211200553, '王宗祥', '2021软件工程2班', 90, 70, 100);
INSERT INTO `project_checks_score` VALUES (5, 20211200556, '王鑫', '2021软件工程1班', 100, 90, 80);
INSERT INTO `project_checks_score` VALUES (6, 20211200558, '王贵萱', '2021软件工程1班', 105, 0, 100);
INSERT INTO `project_checks_score` VALUES (7, 20211200584, '何彦莹', '2021软件工程1班', 98, 80, 100);
INSERT INTO `project_checks_score` VALUES (61, 20211200596, '于舒睿', '2021软件工程2班', 85, 0, 100);
INSERT INTO `project_checks_score` VALUES (62, 20211200598, '张杨', '2021软件工程2班', -7, 0, 100);
INSERT INTO `project_checks_score` VALUES (63, 20211200601, '孙欣欣', '2021软件工程2班', NULL, -40, 100);
INSERT INTO `project_checks_score` VALUES (8, 20211200602, '刘鑫宇', '2021软件工程1班', 105, -20, 0);
INSERT INTO `project_checks_score` VALUES (9, 20211200605, '郑琳', '2021软件工程1班', 98, 60, 100);
INSERT INTO `project_checks_score` VALUES (64, 20211200606, '迟稼铭', '2021软件工程2班', -10, 0, 0);
INSERT INTO `project_checks_score` VALUES (10, 20211200710, '汪康', '2021软件工程1班', 105, 0, 100);
INSERT INTO `project_checks_score` VALUES (65, 20211200711, '章嘉劭', '2021软件工程2班', 93, 50, 100);
INSERT INTO `project_checks_score` VALUES (11, 20211200719, '王鹏', '2021软件工程1班', 98, 90, 100);
INSERT INTO `project_checks_score` VALUES (66, 20211201119, '王福龙', '2021软件工程2班', 80, 70, 100);
INSERT INTO `project_checks_score` VALUES (12, 20211201141, '闫政', '2021软件工程1班', 98, 90, 100);
INSERT INTO `project_checks_score` VALUES (13, 20211201148, '郭会发', '2021软件工程1班', 98, 40, 100);
INSERT INTO `project_checks_score` VALUES (14, 20211201392, '孙可言', '2021软件工程1班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (15, 20211201418, '刘陵', '2021软件工程1班', 105, 80, 100);
INSERT INTO `project_checks_score` VALUES (67, 20211201454, '何海兴', '2021软件工程2班', 93, 60, 100);
INSERT INTO `project_checks_score` VALUES (68, 20211201457, '赵旋', '2021软件工程2班', 105, 50, 100);
INSERT INTO `project_checks_score` VALUES (16, 20211201458, '焦海霞', '2021软件工程1班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (17, 20211201483, '张含锋', '2021软件工程1班', 100, 100, 100);
INSERT INTO `project_checks_score` VALUES (69, 20211201659, '彭锦龙', '2021软件工程2班', 60, 0, 100);
INSERT INTO `project_checks_score` VALUES (70, 20211201766, '李欣欢', '2021软件工程2班', 90, 70, 100);
INSERT INTO `project_checks_score` VALUES (71, 20211201785, '马乐晨', '2021软件工程2班', 90, 0, 100);
INSERT INTO `project_checks_score` VALUES (72, 20211201793, '乔佳昕', '2021软件工程2班', 93, 0, 100);
INSERT INTO `project_checks_score` VALUES (18, 20211201803, '张士博', '2021软件工程1班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (19, 20211201804, '葛怀睿', '2021软件工程1班', 109, 0, 100);
INSERT INTO `project_checks_score` VALUES (20, 20211201806, '刘帅博', '2021软件工程1班', 90, 50, 100);
INSERT INTO `project_checks_score` VALUES (21, 20211201849, '魏继瑶', '2021软件工程1班', 98, 50, 100);
INSERT INTO `project_checks_score` VALUES (73, 20211201867, '付陈瑶', '2021软件工程2班', 60, 90, 100);
INSERT INTO `project_checks_score` VALUES (22, 20211201874, '郭伟康', '2021软件工程1班', 100, -20, 100);
INSERT INTO `project_checks_score` VALUES (23, 20211201875, '王林超', '2021软件工程1班', 60, 0, 100);
INSERT INTO `project_checks_score` VALUES (24, 20211201878, '杨嘉沐', '2021软件工程1班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (74, 20211201890, '常宏伟', '2021软件工程2班', 110, 80, 100);
INSERT INTO `project_checks_score` VALUES (75, 20211201893, '韩森宇', '2021软件工程2班', 90, 90, 100);
INSERT INTO `project_checks_score` VALUES (25, 20211201897, '张锐颀', '2021软件工程1班', 90, 90, 100);
INSERT INTO `project_checks_score` VALUES (26, 20211201899, '刘子轩', '2021软件工程1班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (76, 20211201900, '王腾鑫', '2021软件工程2班', 90, 90, 100);
INSERT INTO `project_checks_score` VALUES (77, 20211201902, '张睿泽', '2021软件工程2班', -5, -40, 100);
INSERT INTO `project_checks_score` VALUES (27, 20211201903, '董美娇', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (28, 20211202068, '常松', '2021软件工程1班', 90, 90, 100);
INSERT INTO `project_checks_score` VALUES (78, 20211202069, '刘庆龙', '2021软件工程2班', 80, -10, 0);
INSERT INTO `project_checks_score` VALUES (79, 20211202072, '邢子阳', '2021软件工程2班', 60, 0, 100);
INSERT INTO `project_checks_score` VALUES (29, 20211202073, '陈浩然', '2021软件工程1班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (80, 20211202079, '祁明扬', '2021软件工程2班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (81, 20211202081, '任靓', '2021软件工程2班', 95, 75, 100);
INSERT INTO `project_checks_score` VALUES (30, 20211202083, '高铎', '2021软件工程1班', 98, 50, 50);
INSERT INTO `project_checks_score` VALUES (82, 20211202090, '姚祥桐', '2021软件工程2班', 95, 110, 100);
INSERT INTO `project_checks_score` VALUES (83, 20211202095, '王雅鑫', '2021软件工程2班', 95, 0, 100);
INSERT INTO `project_checks_score` VALUES (31, 20211202101, '陈广硕', '2021软件工程1班', 105, 0, 100);
INSERT INTO `project_checks_score` VALUES (32, 20211202103, '张瑛琪', '2021软件工程1班', 105, 0, 100);
INSERT INTO `project_checks_score` VALUES (84, 20211202104, '耿唯瀚', '2021软件工程2班', 80, 0, 100);
INSERT INTO `project_checks_score` VALUES (33, 20211202111, '张博', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (85, 20211202112, '李明哲', '2021软件工程2班', 85, -40, 100);
INSERT INTO `project_checks_score` VALUES (34, 20211202125, '黄照凯', '2021软件工程1班', 105, 50, 100);
INSERT INTO `project_checks_score` VALUES (86, 20211202312, '徐婷', '2021软件工程2班', 95, 0, 100);
INSERT INTO `project_checks_score` VALUES (35, 20211202326, '李俊兰', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (87, 20211202355, '支毅博', '2021软件工程2班', 75, -20, 100);
INSERT INTO `project_checks_score` VALUES (88, 20211202362, '赵佳乐', '2021软件工程2班', 60, 0, 100);
INSERT INTO `project_checks_score` VALUES (36, 20211202380, '李轩', '2021软件工程1班', 100, 40, 100);
INSERT INTO `project_checks_score` VALUES (89, 20211202487, '翟翱', '2021软件工程2班', 95, 0, 100);
INSERT INTO `project_checks_score` VALUES (37, 20211202495, '饶峰', '2021软件工程1班', 96, 80, 100);
INSERT INTO `project_checks_score` VALUES (38, 20211202543, '罗民富', '2021软件工程1班', 97, -30, 100);
INSERT INTO `project_checks_score` VALUES (39, 20211202705, '丁金洋', '2021软件工程1班', 98, 0, 100);
INSERT INTO `project_checks_score` VALUES (90, 20211202720, '张书通', '2021软件工程2班', 90, -40, 100);
INSERT INTO `project_checks_score` VALUES (40, 20211202723, '田兆卓', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (41, 20211202724, '王洪福', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (91, 20211202726, '李韩', '2021软件工程2班', 80, 70, 100);
INSERT INTO `project_checks_score` VALUES (92, 20211202730, '郭桐羽', '2021软件工程2班', -20, 0, 100);
INSERT INTO `project_checks_score` VALUES (93, 20211202732, '张宇', '2021软件工程2班', 85, 90, 100);
INSERT INTO `project_checks_score` VALUES (94, 20211202744, '王祉桥', '2021软件工程2班', 110, -20, 100);
INSERT INTO `project_checks_score` VALUES (95, 20211202754, '刘扬', '2021软件工程2班', -10, -35, 100);
INSERT INTO `project_checks_score` VALUES (42, 20211202759, '唐文勃', '2021软件工程1班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (96, 20211202822, '何通海', '2021软件工程2班', 95, 60, 100);
INSERT INTO `project_checks_score` VALUES (97, 20211202855, '任子豪', '2021软件工程2班', 90, 60, 100);
INSERT INTO `project_checks_score` VALUES (43, 20211202868, '孙艺慧', '2021软件工程1班', 100, 90, 100);
INSERT INTO `project_checks_score` VALUES (44, 20211202878, '涂泉源', '2021软件工程1班', 100, 100, 100);
INSERT INTO `project_checks_score` VALUES (98, 20211202881, '吴健南', '2021软件工程2班', 85, 110, 100);
INSERT INTO `project_checks_score` VALUES (45, 20211202900, '陈梦飞', '2021软件工程1班', 100, 70, 100);
INSERT INTO `project_checks_score` VALUES (99, 20211202947, '许孙凯', '2021软件工程2班', 95, 110, 100);
INSERT INTO `project_checks_score` VALUES (100, 20211202948, '白明涛', '2021软件工程2班', 95, 110, 100);
INSERT INTO `project_checks_score` VALUES (46, 20211203012, '王冠涵', '2021软件工程1班', 100, -10, 100);
INSERT INTO `project_checks_score` VALUES (47, 20211203035, '卢平', '2021软件工程1班', 98, 90, 100);
INSERT INTO `project_checks_score` VALUES (48, 20211203038, '刘浩宇', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (101, 20211203042, '信帅权', '2021软件工程2班', 60, -20, 100);
INSERT INTO `project_checks_score` VALUES (102, 20211203047, '邓大卫', '2021软件工程2班', 110, 80, 100);
INSERT INTO `project_checks_score` VALUES (49, 20211203049, '尹春普', '2021软件工程1班', 98, 80, 100);
INSERT INTO `project_checks_score` VALUES (103, 20211203059, '刘思豪', '2021软件工程2班', 93, 0, 100);
INSERT INTO `project_checks_score` VALUES (104, 20211203089, '张义超', '2021软件工程2班', 60, -15, 100);
INSERT INTO `project_checks_score` VALUES (105, 20211203091, '王格格', '2021软件工程2班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (50, 20211203783, '张楠', '2021软件工程1班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (106, 20211203792, '戴明东', '2021软件工程2班', 90, 90, 100);
INSERT INTO `project_checks_score` VALUES (107, 20211203974, '李涵', '2021软件工程2班', 110, 50, 100);
INSERT INTO `project_checks_score` VALUES (108, 20211203978, '栾凯越', '2021软件工程2班', 85, 60, 100);
INSERT INTO `project_checks_score` VALUES (51, 20211203980, '刘佳欣', '2021软件工程1班', 100, 100, 100);
INSERT INTO `project_checks_score` VALUES (52, 20211203983, '郑久彤', '2021软件工程1班', 105, 60, 100);
INSERT INTO `project_checks_score` VALUES (109, 20211203986, '崔惟桓', '2021软件工程2班', -10, -35, 100);
INSERT INTO `project_checks_score` VALUES (110, 20211203987, '刘晨阳', '2021软件工程2班', -10, -40, 100);
INSERT INTO `project_checks_score` VALUES (111, 20211203994, '吴航宇', '2021软件工程2班', -10, 70, 100);
INSERT INTO `project_checks_score` VALUES (112, 20211203996, '夏单祁', '2021软件工程2班', 95, 110, 100);
INSERT INTO `project_checks_score` VALUES (53, 20211204314, '阮龙', '2021软件工程1班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (54, 20211204412, '唐韧', '2021软件工程1班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (55, 20211204414, '周作友', '2021软件工程1班', 90, -30, 100);
INSERT INTO `project_checks_score` VALUES (113, 20211204434, '尹才华', '2021软件工程2班', -10, 0, 100);
INSERT INTO `project_checks_score` VALUES (56, 20211204954, '张溪桐', '2021软件工程1班', 90, 50, 100);
INSERT INTO `project_checks_score` VALUES (114, 20212200919, '何玉', '2021软件工程3班', 110, 75, 100);
INSERT INTO `project_checks_score` VALUES (149, 20212200937, '何紫萱', '2021软件工程4班', 100, 110, 100);
INSERT INTO `project_checks_score` VALUES (150, 20212200947, '梁雷', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (115, 20212200989, '袁晓淋', '2021软件工程3班', 105, 60, 100);
INSERT INTO `project_checks_score` VALUES (116, 20212201080, '曹祝群', '2021软件工程3班', 105, 90, 100);
INSERT INTO `project_checks_score` VALUES (117, 20212201098, '陈前', '2021软件工程3班', 105, 20, 100);
INSERT INTO `project_checks_score` VALUES (151, 20212201128, '吕茂奎', '2021软件工程4班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (118, 20212201146, '杨承璐', '2021软件工程3班', 105, 80, 100);
INSERT INTO `project_checks_score` VALUES (119, 20212201172, '龚相涛', '2021软件工程3班', 95, -30, 100);
INSERT INTO `project_checks_score` VALUES (152, 20212201192, '杨大鹏', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (153, 20212201227, '李有英', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (120, 20212201251, '王志远', '2021软件工程3班', 105, 80, 100);
INSERT INTO `project_checks_score` VALUES (121, 20212201258, '张玉钦', '2021软件工程3班', 90, 0, 100);
INSERT INTO `project_checks_score` VALUES (122, 20212201310, '王藜璇', '2021软件工程3班', 105, 20, 100);
INSERT INTO `project_checks_score` VALUES (154, 20212201312, '蔡昊洋', '2021软件工程4班', 110, -40, 100);
INSERT INTO `project_checks_score` VALUES (155, 20212201313, '赵润萍', '2021软件工程4班', 110, 90, 100);
INSERT INTO `project_checks_score` VALUES (156, 20212201315, '王茂', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (123, 20212201320, '张涛', '2021软件工程3班', 95, 0, 100);
INSERT INTO `project_checks_score` VALUES (157, 20212201321, '李明坤', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (158, 20212201323, '廖雅杰', '2021软件工程4班', 110, 90, 100);
INSERT INTO `project_checks_score` VALUES (124, 20212201324, '郑俊', '2021软件工程3班', 95, -10, 100);
INSERT INTO `project_checks_score` VALUES (159, 20212201326, '张宇', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (125, 20212201330, '李正梅', '2021软件工程3班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (160, 20212201331, '邓信松', '2021软件工程4班', 110, 90, 100);
INSERT INTO `project_checks_score` VALUES (126, 20212201335, '武丽', '2021软件工程3班', 100, 60, 100);
INSERT INTO `project_checks_score` VALUES (161, 20212201336, '欧阳进懿', '2021软件工程4班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (162, 20212201340, '李天建', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (163, 20212201347, '刘沅超', '2021软件工程4班', 100, 110, 100);
INSERT INTO `project_checks_score` VALUES (127, 20212201350, '罗亚婷', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (128, 20212201351, '张文瑞', '2021软件工程3班', 110, 75, 100);
INSERT INTO `project_checks_score` VALUES (164, 20212201355, '王福禄', '2021软件工程4班', 100, 110, 100);
INSERT INTO `project_checks_score` VALUES (165, 20212201359, '张永丽', '2021软件工程4班', 110, 25, 100);
INSERT INTO `project_checks_score` VALUES (129, 20212201360, '邹洪东', '2021软件工程3班', 105, 40, 100);
INSERT INTO `project_checks_score` VALUES (130, 20212201365, '孟维', '2021软件工程3班', 100, 50, 100);
INSERT INTO `project_checks_score` VALUES (166, 20212201366, '陈应仙', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (167, 20212201367, '杨杨', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (168, 20212201369, '杨柠柠', '2021软件工程4班', 110, 25, 100);
INSERT INTO `project_checks_score` VALUES (131, 20212201370, '施嘉鋆', '2021软件工程3班', 100, 0, 100);
INSERT INTO `project_checks_score` VALUES (132, 20212201373, '段周清', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (169, 20212201380, '亚比生', '2021软件工程4班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (133, 20212201382, '段丽萍', '2021软件工程3班', 100, -20, 100);
INSERT INTO `project_checks_score` VALUES (170, 20212201385, '贾栋凯', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (134, 20212201391, '杨周成', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (171, 20212201392, '罗成亮', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (135, 20212201393, '张文腾', '2021软件工程3班', 110, 100, 100);
INSERT INTO `project_checks_score` VALUES (172, 20212201394, '马露优', '2021软件工程4班', 100, 110, 100);
INSERT INTO `project_checks_score` VALUES (173, 20212201397, '王劲尧', '2021软件工程4班', 110, 90, 100);
INSERT INTO `project_checks_score` VALUES (136, 20212201399, '郑洁', '2021软件工程3班', 105, 20, 100);
INSERT INTO `project_checks_score` VALUES (174, 20212201400, '马明静', '2021软件工程4班', 80, 110, 100);
INSERT INTO `project_checks_score` VALUES (137, 20212201401, '徐艺', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (138, 20212201402, '伍吉红', '2021软件工程3班', 105, 80, 100);
INSERT INTO `project_checks_score` VALUES (139, 20212201403, '顾敬文', '2021软件工程3班', 110, 75, 100);
INSERT INTO `project_checks_score` VALUES (140, 20212201404, '吴水仙', '2021软件工程3班', 110, 75, 100);
INSERT INTO `project_checks_score` VALUES (175, 20212201405, '龚琛', '2021软件工程4班', 110, -40, 100);
INSERT INTO `project_checks_score` VALUES (141, 20212201408, '张运', '2021软件工程3班', 105, 40, 100);
INSERT INTO `project_checks_score` VALUES (142, 20212201409, '姜人靖', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (176, 20212201410, '黄荣多', '2021软件工程4班', 110, 25, 100);
INSERT INTO `project_checks_score` VALUES (177, 20212201413, '李强贵', '2021软件工程4班', 95, 110, 100);
INSERT INTO `project_checks_score` VALUES (178, 20212201414, '王晓敏', '2021软件工程4班', 110, 0, 100);
INSERT INTO `project_checks_score` VALUES (143, 20212201417, '陈寿富', '2021软件工程3班', 110, -15, 100);
INSERT INTO `project_checks_score` VALUES (179, 20212201420, '卢仕韦', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (144, 20212201423, '陈玉华', '2021软件工程3班', 110, 75, 100);
INSERT INTO `project_checks_score` VALUES (145, 20212201434, '龚礼东', '2021软件工程3班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (146, 20212201435, '杨宏发', '2021软件工程3班', 100, -20, 100);
INSERT INTO `project_checks_score` VALUES (147, 20212201436, '余晨', '2021软件工程3班', 110, 100, 100);
INSERT INTO `project_checks_score` VALUES (180, 20212201439, '赵昌粉', '2021软件工程4班', 100, 110, 100);
INSERT INTO `project_checks_score` VALUES (181, 20212201441, '茶炳榕', '2021软件工程4班', 110, 110, 100);
INSERT INTO `project_checks_score` VALUES (182, 20212201446, '余书艳', '2021软件工程4班', 110, 25, 100);
INSERT INTO `project_checks_score` VALUES (148, 20212201448, '李瞵昌', '2021软件工程3班', 105, 60, 100);
INSERT INTO `project_checks_score` VALUES (183, 20212201449, '张清远', '2021软件工程4班', 110, 25, 100);

-- ----------------------------
-- Table structure for project_group_basic_info
-- ----------------------------
DROP TABLE IF EXISTS `project_group_basic_info`;
CREATE TABLE `project_group_basic_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '分组号',
  `project_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目id',
  `leader_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '组长',
  `student_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生id',
  `class_grade` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '年级',
  `class_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '班级',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 423 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '项目组基本信息和分数' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project_group_basic_info
-- ----------------------------
INSERT INTO `project_group_basic_info` VALUES (1, '1', '1', '尹春普', '20211203049', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (2, '1', '1', '尹春普', '20211204414', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (3, '1', '1', '尹春普', '20211202543', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (4, '1', '1', '尹春普', '20211202495', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (5, '1', '1', '尹春普', '20211200551', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (6, '1', '1', '尹春普', '20191202255', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (7, '2', '2', '闫政', '20211201148', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (8, '2', '2', '闫政', '20211203035', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (9, '2', '2', '闫政', '20211202073', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (10, '2', '2', '闫政', '20211201141', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (11, '2', '2', '闫政', '20211202068', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (12, '2', '2', '闫政', '20211201897', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (13, '2', '2', '闫政', '20211202759', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (14, '3', '3', '丁金洋', '20211202900', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (15, '3', '3', '丁金洋', '20211203783', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (16, '3', '3', '丁金洋', '20211201874', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (17, '3', '3', '丁金洋', '20201202139', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (18, '3', '3', '丁金洋', '20211201803', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (19, '3', '3', '丁金洋', '20211204954', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (20, '3', '3', '丁金洋', ' 20211202705', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (21, '4', '4', '刘佳欣', '20211201483', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (22, '4', '4', '刘佳欣', '20211201392', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (23, '4', '4', '刘佳欣', '20211202878', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (24, '4', '4', '刘佳欣', '20211200384', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (25, '4', '4', '刘佳欣', '20211203980', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (26, '4', '4', '刘佳欣', '20211201806', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (27, '5', '5', '张瑛琪', '20211200558', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (28, '5', '5', '张瑛琪', '20211200584', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (29, '5', '5', '张瑛琪', '20211200602', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (30, '5', '5', '张瑛琪', '20211201418', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (31, '5', '5', '张瑛琪', '20211202101', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (32, '5', '5', '张瑛琪', '20211202103', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (33, '5', '5', '张瑛琪', '20211202125', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (34, '6', '6', '刘子轩', '20211202083', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (35, '6', '6', '刘子轩', '20211201849', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (36, '6', '6', '刘子轩', '20211202868', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (37, '6', '6', '刘子轩', '20211201458', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (38, '6', '6', '刘子轩', '20211202380', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (39, '6', '6', '刘子轩', '20211201899', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (40, '6', '6', '刘子轩', '20211204412', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (41, '7', '7', '王鹏', '2021120710', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (42, '7', '7', '王鹏', '20211201804', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (43, '7', '7', '王鹏', '20211200719', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (44, '7', '7', '王鹏', '20211202724', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (45, '7', '7', '王鹏', '20211200605', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (46, '7', '7', '王鹏', '20211202723', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (47, '7', '7', '王鹏', '20211202326', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (48, '8', '8', '王冠涵', '20211203012', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (49, '8', '8', '王冠涵', '20211202111', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (50, '8', '8', '王冠涵', '20211203983', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (51, '8', '8', '王冠涵', '20211204314', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (52, '8', '8', '王冠涵', '20211201903', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (53, '8', '8', '王冠涵', '20211203038', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (54, '8', '8', '王冠涵', '20211200556', '2021级', '软件工程1班');
INSERT INTO `project_group_basic_info` VALUES (55, '1', '1', '尹才华', '20211204434', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (56, '1', '1', '尹才华', '20181203922', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (57, '1', '1', '尹才华', '20211203987', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (58, '1', '1', '尹才华', '20211203994', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (59, '1', '1', '尹才华', '20211200553', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (60, '1', '1', '尹才华', '20211202720', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (61, '1', '1', '尹才华', '20211202112', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (62, '1', '1', '尹才华', '20211201766', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (63, '2', '2', '王腾鑫', '20211201900', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (64, '2', '2', '王腾鑫', '20211201893', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (65, '2', '2', '王腾鑫', '20211202362', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (66, '2', '2', '王腾鑫', '20211202732', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (67, '2', '2', '王腾鑫', '20211203792', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (68, '2', '2', '王腾鑫', '20211201867', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (69, '2', '2', '王腾鑫', '20211203978', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (70, '3', '3', '王格格', '20211202744', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (71, '3', '3', '王格格', '20211202079', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (72, '3', '3', '王格格', '20211203974', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (73, '3', '3', '王格格', '20211201457', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (74, '3', '3', '王格格', '20211201890', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (75, '3', '3', '王格格', '20211203047', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (76, '3', '3', '王格格', '20211203091', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (77, '4', '4', '章嘉劭', '20211200711', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (78, '4', '4', '章嘉劭', '20211200385', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (79, '4', '4', '章嘉劭', '20211200598', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (80, '4', '4', '章嘉劭', '20211200601', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (81, '4', '4', '章嘉劭', '20211201454', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (82, '4', '4', '章嘉劭', '20211201793', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (83, '4', '4', '章嘉劭', '20211203059', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (84, '5', '5', '王雅鑫', '20211202822', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (85, '5', '5', '王雅鑫', '20211202855', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (86, '5', '5', '王雅鑫', '20211202487', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (87, '5', '5', '王雅鑫', '20191202610', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (88, '5', '5', '王雅鑫', '20211202095', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (89, '5', '5', '王雅鑫', '20211202312', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (90, '5', '5', '王雅鑫', '20211201902', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (91, '6', '6', '马乐晨', '20211201785', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (92, '6', '6', '马乐晨', '20211202104', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (93, '6', '6', '马乐晨', '20211200596', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (94, '6', '6', '马乐晨', '20211200606', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (95, '6', '6', '马乐晨', '20211202069', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (96, '6', '6', '马乐晨', '20211202754', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (97, '6', '6', '马乐晨', '20211203986', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (98, '7', '7', '李韩', '20211202726', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (99, '7', '7', '李韩', '20211201659', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (100, '7', '7', '李韩', '20211202355', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (101, '7', '7', '李韩', '20211201119', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (102, '7', '7', '李韩', '20211202072', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (103, '7', '7', '李韩', '20211203042', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (104, '7', '7', '李韩', '20211202730', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (105, '8', '8', '姚祥桐', '20211203996', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (106, '8', '8', '姚祥桐', '20211202081', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (107, '8', '8', '姚祥桐', '20211202948', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (108, '8', '8', '姚祥桐', '20211203089', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (109, '8', '8', '姚祥桐', '20211202090', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (110, '8', '8', '姚祥桐', '20211202881', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (111, '8', '8', '姚祥桐', '20211202947', '2021级', '软件工程2班');
INSERT INTO `project_group_basic_info` VALUES (112, '1', '1', '陈前', '20212201408', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (113, '1', '1', '陈前', '20212201258', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (114, '1', '1', '陈前', '20212201399', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (115, '1', '1', '陈前', '20212201310', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (116, '1', '1', '陈前', '20212201365', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (117, '1', '1', '陈前', '20212201360', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (118, '1', '1', '陈前', '20212201098', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (119, '2', '2', '杨宏发', '20212201382', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (120, '2', '2', '杨宏发', '20212201172', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (121, '2', '2', '杨宏发', '20212201335', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (122, '2', '2', '杨宏发', '20212201330', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (123, '2', '2', '杨宏发', '20212201370', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (124, '2', '2', '杨宏发', '20212201320', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (125, '2', '2', '杨宏发', '20212201435', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (126, '3', '3', '陈寿富', '20212201417', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (127, '3', '3', '陈寿富', '20212201350', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (128, '3', '3', '陈寿富', '20212201373', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (129, '3', '3', '陈寿富', '20212201391', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (130, '3', '3', '陈寿富', '20212201401', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (131, '3', '3', '陈寿富', '20212201409', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (132, '3', '3', '陈寿富', '20212201434', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (133, '4', '4', '王志远', '20212201251', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (134, '4', '4', '王志远', '20212200989', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (135, '4', '4', '王志远', '20212201324', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (136, '4', '4', '王志远', '20212201080', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (137, '4', '4', '王志远', '20212201146', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (138, '4', '4', '王志远', '20212201448', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (139, '4', '4', '王志远', '20212201402', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (140, '5', '5', '何玉', '20212200919', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (141, '5', '5', '何玉', '20212201404', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (142, '5', '5', '何玉', '20212201436', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (143, '5', '5', '何玉', '20212201351', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (144, '5', '5', '何玉', '20212201423', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (145, '5', '5', '何玉', '20212201403', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (146, '5', '5', '何玉', '20212201393', '2021级', '软件工程3班');
INSERT INTO `project_group_basic_info` VALUES (147, '1', '1', '欧阳进懿', '20212201128', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (148, '1', '1', '欧阳进懿', '20212201312', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (149, '1', '1', '欧阳进懿', '20212201336', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (150, '1', '1', '欧阳进懿', '20212201340', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (151, '1', '1', '欧阳进懿', '20212201380', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (152, '1', '1', '欧阳进懿', '20212201405', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (153, '1', '1', '欧阳进懿', '20212201414', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (154, '2', '2', '张永丽', '20212201359', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (155, '2', '2', '张永丽', '20212201397', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (156, '2', '2', '张永丽', '20212201446', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (157, '2', '2', '张永丽', '20212201313', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (158, '2', '2', '张永丽', '20212201410', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (159, '2', '2', '张永丽', '20212201449', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (160, '2', '2', '张永丽', '20212201369', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (161, '3', '3', '王茂', '20212200947', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (162, '3', '3', '王茂', '20212201315', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (163, '3', '3', '王茂', '20212201323', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (164, '3', '3', '王茂', '20212201331', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (165, '3', '3', '王茂', '20212201385', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (166, '3', '3', '王茂', '20212201392', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (167, '3', '3', '王茂', '20212201420', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (168, '4', '4', '陈应仙', '20212201366', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (169, '4', '4', '陈应仙', '20212201321', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (170, '4', '4', '陈应仙', '20212201227', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (171, '4', '4', '陈应仙', '20212201441', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (172, '4', '4', '陈应仙', '20212201367', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (173, '4', '4', '陈应仙', '20212201326', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (174, '4', '4', '陈应仙', '20212201192', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (175, '5', '5', '何紫萱', '20212200937', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (176, '5', '5', '何紫萱', '20212201400', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (177, '5', '5', '何紫萱', '20212201394', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (178, '5', '5', '何紫萱', '20212201439', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (179, '5', '5', '何紫萱', '20212201355', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (180, '5', '5', '何紫萱', '20212201413', '2021级', '软件工程4班');
INSERT INTO `project_group_basic_info` VALUES (181, '5', '5', '何紫萱', '20212201347', '2021级', '软件工程4班');

-- ----------------------------
-- Table structure for project_task
-- ----------------------------
DROP TABLE IF EXISTS `project_task`;
CREATE TABLE `project_task`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NULL DEFAULT NULL COMMENT '项目ID',
  `project_task` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目任务',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 79 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '项目任务' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project_task
-- ----------------------------
INSERT INTO `project_task` VALUES (1, 1, '用户注册');
INSERT INTO `project_task` VALUES (2, 1, '用户登录');
INSERT INTO `project_task` VALUES (3, 1, '新闻显示');
INSERT INTO `project_task` VALUES (4, 1, '产品信息展示');
INSERT INTO `project_task` VALUES (5, 1, '下载中心');
INSERT INTO `project_task` VALUES (6, 1, '用户留言');
INSERT INTO `project_task` VALUES (7, 1, '退出系统');
INSERT INTO `project_task` VALUES (8, 1, '新闻管理');
INSERT INTO `project_task` VALUES (9, 1, '产品信息管理');
INSERT INTO `project_task` VALUES (10, 1, '招聘信息管理');
INSERT INTO `project_task` VALUES (11, 1, '用户管理');
INSERT INTO `project_task` VALUES (12, 2, '基础资料设置');
INSERT INTO `project_task` VALUES (13, 2, '客户信息管理');
INSERT INTO `project_task` VALUES (14, 2, '收货管理');
INSERT INTO `project_task` VALUES (15, 2, '单据查找');
INSERT INTO `project_task` VALUES (16, 2, '派件管理');
INSERT INTO `project_task` VALUES (17, 2, '报表统计');
INSERT INTO `project_task` VALUES (18, 3, '用户注册');
INSERT INTO `project_task` VALUES (19, 3, '用户登录');
INSERT INTO `project_task` VALUES (20, 3, '影片资讯');
INSERT INTO `project_task` VALUES (21, 3, '影城介绍');
INSERT INTO `project_task` VALUES (22, 3, '影片归档查询');
INSERT INTO `project_task` VALUES (23, 3, '在线购票');
INSERT INTO `project_task` VALUES (24, 3, '会员专区');
INSERT INTO `project_task` VALUES (25, 3, '影片管理');
INSERT INTO `project_task` VALUES (26, 3, '会员管理');
INSERT INTO `project_task` VALUES (27, 3, '系统参数管理');
INSERT INTO `project_task` VALUES (28, 4, '用户注册');
INSERT INTO `project_task` VALUES (29, 4, '用户登录');
INSERT INTO `project_task` VALUES (30, 4, '团品显示');
INSERT INTO `project_task` VALUES (31, 4, '购买');
INSERT INTO `project_task` VALUES (32, 4, '用户评价');
INSERT INTO `project_task` VALUES (33, 4, '退出系统');
INSERT INTO `project_task` VALUES (34, 4, '团品管理');
INSERT INTO `project_task` VALUES (35, 4, '用户账户管理');
INSERT INTO `project_task` VALUES (36, 4, '退货管理');
INSERT INTO `project_task` VALUES (37, 5, '用户注册');
INSERT INTO `project_task` VALUES (38, 5, '用户登录');
INSERT INTO `project_task` VALUES (39, 5, '酒店查询');
INSERT INTO `project_task` VALUES (40, 5, '酒店预定');
INSERT INTO `project_task` VALUES (41, 5, '用户留言');
INSERT INTO `project_task` VALUES (42, 5, '退出系统');
INSERT INTO `project_task` VALUES (43, 5, '订单管理');
INSERT INTO `project_task` VALUES (44, 5, '账户管理');
INSERT INTO `project_task` VALUES (45, 5, '个人信息管理');
INSERT INTO `project_task` VALUES (46, 5, '酒店管理');
INSERT INTO `project_task` VALUES (47, 6, '用户管理');
INSERT INTO `project_task` VALUES (48, 6, '信息管理');
INSERT INTO `project_task` VALUES (49, 6, '合同管理');
INSERT INTO `project_task` VALUES (50, 6, '销售管理');
INSERT INTO `project_task` VALUES (51, 7, '用户权限管理');
INSERT INTO `project_task` VALUES (52, 7, '菜单管理');
INSERT INTO `project_task` VALUES (53, 7, '订餐管理');
INSERT INTO `project_task` VALUES (54, 7, '会员管理');
INSERT INTO `project_task` VALUES (55, 7, '购物车管理');
INSERT INTO `project_task` VALUES (57, 2, '登录注册');
INSERT INTO `project_task` VALUES (58, 3, '退出系统');
INSERT INTO `project_task` VALUES (59, 5, '退货管理');
INSERT INTO `project_task` VALUES (60, 5, '团品显示');
INSERT INTO `project_task` VALUES (61, 5, '团品管理');
INSERT INTO `project_task` VALUES (62, 5, '退出系统');
INSERT INTO `project_task` VALUES (63, 5, '用户评价');
INSERT INTO `project_task` VALUES (64, 5, '用户注册');
INSERT INTO `project_task` VALUES (65, 5, '用户登录');
INSERT INTO `project_task` VALUES (66, 8, '管理模块-分类管理\r');
INSERT INTO `project_task` VALUES (67, 8, '专家模块-个人管理\r');
INSERT INTO `project_task` VALUES (68, 8, '管理模块-个人管理\r');
INSERT INTO `project_task` VALUES (69, 8, '用户模块\r');
INSERT INTO `project_task` VALUES (70, 8, '管理模块-专家管理\r');
INSERT INTO `project_task` VALUES (71, 8, '管理模块-管理登录\r');
INSERT INTO `project_task` VALUES (72, 8, '稿件管理\r');
INSERT INTO `project_task` VALUES (73, 8, '专家模块-专家登录\r');
INSERT INTO `project_task` VALUES (74, 8, '待审作品\r');
INSERT INTO `project_task` VALUES (75, 8, '编辑模块\r');
INSERT INTO `project_task` VALUES (76, 6, '网页页面设计\r');
INSERT INTO `project_task` VALUES (77, 6, '项目测试和编写测试报告\r');
INSERT INTO `project_task` VALUES (78, 6, '数据库设计');

-- ----------------------------
-- Table structure for project_task_student
-- ----------------------------
DROP TABLE IF EXISTS `project_task_student`;
CREATE TABLE `project_task_student`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stu_id` bigint NULL DEFAULT NULL,
  `project_id` int NULL DEFAULT NULL,
  `project_task_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 438 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '项目、项目任务、学生关系表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project_task_student
-- ----------------------------
INSERT INTO `project_task_student` VALUES (182, 20211203049, 1, 11);
INSERT INTO `project_task_student` VALUES (183, 20211203049, 1, 1);
INSERT INTO `project_task_student` VALUES (184, 20211203049, 1, 2);
INSERT INTO `project_task_student` VALUES (185, 20211203049, 1, 7);
INSERT INTO `project_task_student` VALUES (186, 20211202068, 2, 16);
INSERT INTO `project_task_student` VALUES (187, 20211202900, 3, 18);
INSERT INTO `project_task_student` VALUES (188, 20211202900, 3, 19);
INSERT INTO `project_task_student` VALUES (189, 20191202255, 1, 10);
INSERT INTO `project_task_student` VALUES (190, 20211200551, 1, 6);
INSERT INTO `project_task_student` VALUES (191, 20211200551, 1, 9);
INSERT INTO `project_task_student` VALUES (192, 20211202724, 7, 52);
INSERT INTO `project_task_student` VALUES (193, 20211200719, 7, 52);
INSERT INTO `project_task_student` VALUES (194, 20211200584, 5, 41);
INSERT INTO `project_task_student` VALUES (195, 20211200558, 5, 43);
INSERT INTO `project_task_student` VALUES (196, 20211203980, 4, 32);
INSERT INTO `project_task_student` VALUES (197, 20211202073, 2, 12);
INSERT INTO `project_task_student` VALUES (198, 20212201315, 3, 22);
INSERT INTO `project_task_student` VALUES (199, 20212201315, 3, 23);
INSERT INTO `project_task_student` VALUES (200, 20211202326, 7, 55);
INSERT INTO `project_task_student` VALUES (201, 20212201394, 5, 37);
INSERT INTO `project_task_student` VALUES (202, 20212201394, 5, 42);
INSERT INTO `project_task_student` VALUES (203, 20211202072, 7, 54);
INSERT INTO `project_task_student` VALUES (204, 20211201766, 1, 1);
INSERT INTO `project_task_student` VALUES (205, 20211201766, 1, 2);
INSERT INTO `project_task_student` VALUES (206, 20211202947, 8, 75);
INSERT INTO `project_task_student` VALUES (207, 20211202868, 6, 77);
INSERT INTO `project_task_student` VALUES (208, 20211202868, 6, 78);
INSERT INTO `project_task_student` VALUES (209, 20211202868, 6, 48);
INSERT INTO `project_task_student` VALUES (210, 20211202868, 6, 76);
INSERT INTO `project_task_student` VALUES (211, 20211200384, 4, 35);
INSERT INTO `project_task_student` VALUES (212, 20211201900, 2, 14);
INSERT INTO `project_task_student` VALUES (213, 20211201893, 2, 13);
INSERT INTO `project_task_student` VALUES (214, 20181203922, 1, 8);
INSERT INTO `project_task_student` VALUES (215, 20211202881, 8, 73);
INSERT INTO `project_task_student` VALUES (216, 20211202881, 8, 74);
INSERT INTO `project_task_student` VALUES (217, 20211202090, 8, 68);
INSERT INTO `project_task_student` VALUES (218, 20211202090, 8, 71);
INSERT INTO `project_task_student` VALUES (219, 20211202090, 8, 72);
INSERT INTO `project_task_student` VALUES (220, 20211200385, 4, 36);
INSERT INTO `project_task_student` VALUES (221, 20211202705, 3, 21);
INSERT INTO `project_task_student` VALUES (222, 20212201335, 2, 13);
INSERT INTO `project_task_student` VALUES (223, 20212201397, 2, 57);
INSERT INTO `project_task_student` VALUES (224, 20212201397, 2, 14);
INSERT INTO `project_task_student` VALUES (225, 20211203059, 4, 28);
INSERT INTO `project_task_student` VALUES (226, 20211202732, 2, 12);
INSERT INTO `project_task_student` VALUES (227, 20211202103, 5, 44);
INSERT INTO `project_task_student` VALUES (228, 20211202103, 5, 45);
INSERT INTO `project_task_student` VALUES (229, 20211202101, 5, 60);
INSERT INTO `project_task_student` VALUES (230, 20211202101, 5, 61);
INSERT INTO `project_task_student` VALUES (231, 20211202101, 5, 40);
INSERT INTO `project_task_student` VALUES (232, 20211201418, 5, 46);
INSERT INTO `project_task_student` VALUES (233, 20211201418, 5, 39);
INSERT INTO `project_task_student` VALUES (234, 20212201326, 4, 28);
INSERT INTO `project_task_student` VALUES (235, 20212201446, 2, 13);
INSERT INTO `project_task_student` VALUES (236, 20212201446, 2, 57);
INSERT INTO `project_task_student` VALUES (238, 20212201446, 2, 15);
INSERT INTO `project_task_student` VALUES (239, 20212201439, 5, 43);
INSERT INTO `project_task_student` VALUES (240, 20212201400, 5, 38);
INSERT INTO `project_task_student` VALUES (241, 20212201400, 5, 42);
INSERT INTO `project_task_student` VALUES (242, 20212201449, 2, 17);
INSERT INTO `project_task_student` VALUES (243, 20212201313, 2, 57);
INSERT INTO `project_task_student` VALUES (244, 20212201313, 2, 15);
INSERT INTO `project_task_student` VALUES (245, 20212201410, 2, 57);
INSERT INTO `project_task_student` VALUES (246, 20212201410, 2, 14);
INSERT INTO `project_task_student` VALUES (247, 20212201369, 2, 12);
INSERT INTO `project_task_student` VALUES (248, 20211201803, 3, 24);
INSERT INTO `project_task_student` VALUES (249, 20211201803, 3, 26);
INSERT INTO `project_task_student` VALUES (250, 20212201359, 2, 16);
INSERT INTO `project_task_student` VALUES (251, 20211201659, 7, 53);
INSERT INTO `project_task_student` VALUES (252, 20212201321, 4, 35);
INSERT INTO `project_task_student` VALUES (253, 20211202726, 7, 51);
INSERT INTO `project_task_student` VALUES (254, NULL, NULL, NULL);
INSERT INTO `project_task_student` VALUES (255, 20212201392, 3, 58);
INSERT INTO `project_task_student` VALUES (256, 20212201392, 3, 18);
INSERT INTO `project_task_student` VALUES (257, 20212201392, 3, 19);
INSERT INTO `project_task_student` VALUES (258, 20212201385, 3, 26);
INSERT INTO `project_task_student` VALUES (259, 20212201192, 4, 33);
INSERT INTO `project_task_student` VALUES (260, 20212201355, 5, 41);
INSERT INTO `project_task_student` VALUES (261, 20212201413, 5, 45);
INSERT INTO `project_task_student` VALUES (262, 20212201367, 4, 36);
INSERT INTO `project_task_student` VALUES (263, 20212201367, 4, 29);
INSERT INTO `project_task_student` VALUES (264, 20211203035, 2, 17);
INSERT INTO `project_task_student` VALUES (265, 20211202723, 7, 54);
INSERT INTO `project_task_student` VALUES (266, 20211202083, 6, 77);
INSERT INTO `project_task_student` VALUES (267, 20211202083, 6, 78);
INSERT INTO `project_task_student` VALUES (268, 20211202083, 6, 47);
INSERT INTO `project_task_student` VALUES (269, 20211202083, 6, 76);
INSERT INTO `project_task_student` VALUES (270, 20211202362, 2, 15);
INSERT INTO `project_task_student` VALUES (271, 20211201119, 7, 55);
INSERT INTO `project_task_student` VALUES (272, 20211202081, 8, 67);
INSERT INTO `project_task_student` VALUES (273, 20212201146, 4, 29);
INSERT INTO `project_task_student` VALUES (274, 20212201402, 4, 28);
INSERT INTO `project_task_student` VALUES (275, 20191202610, 5, 43);
INSERT INTO `project_task_student` VALUES (276, 20212201436, 5, 37);
INSERT INTO `project_task_student` VALUES (277, 20212201436, 5, 38);
INSERT INTO `project_task_student` VALUES (278, 20212201436, 5, 64);
INSERT INTO `project_task_student` VALUES (279, 20212201436, 5, 65);
INSERT INTO `project_task_student` VALUES (280, 20211203042, 7, 52);
INSERT INTO `project_task_student` VALUES (281, 20211202730, 7, 51);
INSERT INTO `project_task_student` VALUES (282, 20212200919, 5, 41);
INSERT INTO `project_task_student` VALUES (283, 20212200919, 5, 42);
INSERT INTO `project_task_student` VALUES (284, 20212201393, 5, 45);
INSERT INTO `project_task_student` VALUES (285, 20212201404, 5, 43);
INSERT INTO `project_task_student` VALUES (286, 20212201423, 5, 39);
INSERT INTO `project_task_student` VALUES (287, 20212201423, 5, 40);
INSERT INTO `project_task_student` VALUES (288, 20212201351, 5, 46);
INSERT INTO `project_task_student` VALUES (289, 20212201403, 5, 44);
INSERT INTO `project_task_student` VALUES (290, 20212201324, 4, 33);
INSERT INTO `project_task_student` VALUES (291, 20212201324, 4, 36);
INSERT INTO `project_task_student` VALUES (292, 20211202112, 1, 10);
INSERT INTO `project_task_student` VALUES (293, 20211200553, 1, 4);
INSERT INTO `project_task_student` VALUES (294, 20212201382, 2, 15);
INSERT INTO `project_task_student` VALUES (295, 20211202487, 5, 41);
INSERT INTO `project_task_student` VALUES (296, 20211202487, 5, 42);
INSERT INTO `project_task_student` VALUES (297, 20212201320, 2, 12);
INSERT INTO `project_task_student` VALUES (298, 20212201417, 3, 21);
INSERT INTO `project_task_student` VALUES (299, 20211202720, 1, 11);
INSERT INTO `project_task_student` VALUES (300, 20211202855, 5, 39);
INSERT INTO `project_task_student` VALUES (301, 20211202855, 5, 40);
INSERT INTO `project_task_student` VALUES (302, 20211202095, 5, 44);
INSERT INTO `project_task_student` VALUES (303, 20211202095, 5, 60);
INSERT INTO `project_task_student` VALUES (304, 20211202095, 5, 61);
INSERT INTO `project_task_student` VALUES (305, 20211202312, 5, 45);
INSERT INTO `project_task_student` VALUES (306, 20212201350, 3, 58);
INSERT INTO `project_task_student` VALUES (307, 20212201350, 3, 18);
INSERT INTO `project_task_student` VALUES (308, 20212201350, 3, 19);
INSERT INTO `project_task_student` VALUES (309, 20212201373, 3, 22);
INSERT INTO `project_task_student` VALUES (310, 20212201391, 3, 23);
INSERT INTO `project_task_student` VALUES (311, 20212201391, 3, 25);
INSERT INTO `project_task_student` VALUES (312, 20212201401, 3, 24);
INSERT INTO `project_task_student` VALUES (313, 20212201401, 3, 26);
INSERT INTO `project_task_student` VALUES (314, 20212201409, 3, 25);
INSERT INTO `project_task_student` VALUES (315, 20212201409, 3, 20);
INSERT INTO `project_task_student` VALUES (316, 20212201434, 3, 25);
INSERT INTO `project_task_student` VALUES (317, 20212201434, 3, 58);
INSERT INTO `project_task_student` VALUES (318, 20212201434, 3, 27);
INSERT INTO `project_task_student` VALUES (319, 20211202822, 5, 37);
INSERT INTO `project_task_student` VALUES (320, 20211202822, 5, 38);
INSERT INTO `project_task_student` VALUES (321, 20212201330, 2, 16);
INSERT INTO `project_task_student` VALUES (322, 20212201370, 2, 14);
INSERT INTO `project_task_student` VALUES (323, 20211200711, 4, 33);
INSERT INTO `project_task_student` VALUES (324, 20211200711, 4, 29);
INSERT INTO `project_task_student` VALUES (325, 20211201793, 4, 31);
INSERT INTO `project_task_student` VALUES (326, 20211200598, 4, 34);
INSERT INTO `project_task_student` VALUES (327, 20212201435, 2, 17);
INSERT INTO `project_task_student` VALUES (328, 20212201172, 2, 17);
INSERT INTO `project_task_student` VALUES (329, 20212201251, 4, 35);
INSERT INTO `project_task_student` VALUES (330, 20212201441, 4, 32);
INSERT INTO `project_task_student` VALUES (331, 20211203047, 3, 58);
INSERT INTO `project_task_student` VALUES (332, 20211203047, 3, 27);
INSERT INTO `project_task_student` VALUES (333, 20211203047, 3, 18);
INSERT INTO `project_task_student` VALUES (334, 20211203047, 3, 19);
INSERT INTO `project_task_student` VALUES (335, 20211201457, 3, 24);
INSERT INTO `project_task_student` VALUES (336, 20211201457, 3, 58);
INSERT INTO `project_task_student` VALUES (337, 20211201457, 3, 26);
INSERT INTO `project_task_student` VALUES (338, 20211201457, 3, 27);
INSERT INTO `project_task_student` VALUES (339, 20211203091, 3, 23);
INSERT INTO `project_task_student` VALUES (340, 20211203091, 3, 58);
INSERT INTO `project_task_student` VALUES (341, 20211203091, 3, 27);
INSERT INTO `project_task_student` VALUES (342, 20211201890, 3, 25);
INSERT INTO `project_task_student` VALUES (343, 20211201890, 3, 58);
INSERT INTO `project_task_student` VALUES (344, 20211201890, 3, 27);
INSERT INTO `project_task_student` VALUES (345, 20211203974, 3, 58);
INSERT INTO `project_task_student` VALUES (346, 20211203974, 3, 27);
INSERT INTO `project_task_student` VALUES (347, 20211203974, 3, 20);
INSERT INTO `project_task_student` VALUES (348, 20211203974, 3, 21);
INSERT INTO `project_task_student` VALUES (349, 20211202744, 3, 22);
INSERT INTO `project_task_student` VALUES (350, 20211202744, 3, 58);
INSERT INTO `project_task_student` VALUES (351, 20211202744, 3, 27);
INSERT INTO `project_task_student` VALUES (352, 20211202079, 3, 58);
INSERT INTO `project_task_student` VALUES (353, 20211202079, 3, 27);
INSERT INTO `project_task_student` VALUES (354, 20211204412, 6, 77);
INSERT INTO `project_task_student` VALUES (355, 20211204412, 6, 78);
INSERT INTO `project_task_student` VALUES (356, 20211204412, 6, 50);
INSERT INTO `project_task_student` VALUES (357, 20211204412, 6, 76);
INSERT INTO `project_task_student` VALUES (358, 20211202380, 6, 77);
INSERT INTO `project_task_student` VALUES (359, 20211202380, 6, 78);
INSERT INTO `project_task_student` VALUES (360, 20211202380, 6, 49);
INSERT INTO `project_task_student` VALUES (361, 20211202380, 6, 76);
INSERT INTO `project_task_student` VALUES (362, 20211201849, 6, 77);
INSERT INTO `project_task_student` VALUES (363, 20211201849, 6, 78);
INSERT INTO `project_task_student` VALUES (364, 20211201849, 6, 47);
INSERT INTO `project_task_student` VALUES (365, 20211201849, 6, 76);
INSERT INTO `project_task_student` VALUES (366, 20211204954, 3, 22);
INSERT INTO `project_task_student` VALUES (367, 20211201899, 6, 77);
INSERT INTO `project_task_student` VALUES (368, 20211201899, 6, 78);
INSERT INTO `project_task_student` VALUES (369, 20211201899, 6, 49);
INSERT INTO `project_task_student` VALUES (370, 20211201899, 6, 76);
INSERT INTO `project_task_student` VALUES (371, 20211200605, 7, 53);
INSERT INTO `project_task_student` VALUES (372, 20211202495, 1, 8);
INSERT INTO `project_task_student` VALUES (373, 20211201392, 4, 36);
INSERT INTO `project_task_student` VALUES (374, 20211203783, 3, 25);
INSERT INTO `project_task_student` VALUES (375, 20211201148, 2, 13);
INSERT INTO `project_task_student` VALUES (376, 20211201897, 2, 14);
INSERT INTO `project_task_student` VALUES (377, 20211201141, 2, 15);
INSERT INTO `project_task_student` VALUES (378, 20211203792, 2, 17);
INSERT INTO `project_task_student` VALUES (379, 20211201902, 5, 46);
INSERT INTO `project_task_student` VALUES (380, 20211201867, 2, 12);
INSERT INTO `project_task_student` VALUES (381, 20211202948, 8, 68);
INSERT INTO `project_task_student` VALUES (382, 20211202948, 8, 69);
INSERT INTO `project_task_student` VALUES (383, 20211202948, 8, 72);
INSERT INTO `project_task_student` VALUES (384, 20211203996, 8, 66);
INSERT INTO `project_task_student` VALUES (385, 20212201080, 4, 32);
INSERT INTO `project_task_student` VALUES (386, 20212201098, 1, 3);
INSERT INTO `project_task_student` VALUES (387, 20212201098, 1, 8);
INSERT INTO `project_task_student` VALUES (388, 20212200989, 4, 30);
INSERT INTO `project_task_student` VALUES (389, 20212200989, 4, 31);
INSERT INTO `project_task_student` VALUES (390, 20212201365, 1, 1);
INSERT INTO `project_task_student` VALUES (391, 20212201365, 1, 2);
INSERT INTO `project_task_student` VALUES (392, 20212201399, 1, 10);
INSERT INTO `project_task_student` VALUES (393, 20211203994, 1, 8);
INSERT INTO `project_task_student` VALUES (394, 20212201310, 1, 4);
INSERT INTO `project_task_student` VALUES (395, 20212201310, 1, 9);
INSERT INTO `project_task_student` VALUES (396, 20211203987, 1, 6);
INSERT INTO `project_task_student` VALUES (397, 20211204434, 1, 5);
INSERT INTO `project_task_student` VALUES (398, 20212201420, 3, 27);
INSERT INTO `project_task_student` VALUES (399, 20212201336, 1, 11);
INSERT INTO `project_task_student` VALUES (400, 20212201336, 1, 2);
INSERT INTO `project_task_student` VALUES (401, 20211203038, 8, 68);
INSERT INTO `project_task_student` VALUES (402, 20211203038, 8, 69);
INSERT INTO `project_task_student` VALUES (403, 20211203012, 8, 70);
INSERT INTO `project_task_student` VALUES (404, 20211203012, 8, 71);
INSERT INTO `project_task_student` VALUES (405, 20211204314, 8, 67);
INSERT INTO `project_task_student` VALUES (406, 20211204314, 8, 72);
INSERT INTO `project_task_student` VALUES (407, 20211202111, 8, 69);
INSERT INTO `project_task_student` VALUES (408, 20211202111, 8, 71);
INSERT INTO `project_task_student` VALUES (409, 20212201405, 1, 4);
INSERT INTO `project_task_student` VALUES (410, 20212201405, 1, 9);
INSERT INTO `project_task_student` VALUES (411, 20212201312, 1, 5);
INSERT INTO `project_task_student` VALUES (412, 20212201312, 1, 9);
INSERT INTO `project_task_student` VALUES (413, 20212201380, 1, 7);
INSERT INTO `project_task_student` VALUES (414, 20212201380, 1, 10);
INSERT INTO `project_task_student` VALUES (415, 20212201366, 4, 34);
INSERT INTO `project_task_student` VALUES (416, 20212201366, 4, 30);
INSERT INTO `project_task_student` VALUES (417, 20212201128, 1, 3);
INSERT INTO `project_task_student` VALUES (418, 20212201128, 1, 8);
INSERT INTO `project_task_student` VALUES (419, 20211200556, 8, 69);
INSERT INTO `project_task_student` VALUES (420, 20211200556, 8, 73);
INSERT INTO `project_task_student` VALUES (421, 20212201414, 1, 1);
INSERT INTO `project_task_student` VALUES (422, 20212201414, 1, 6);
INSERT INTO `project_task_student` VALUES (423, 20211200596, 6, 77);
INSERT INTO `project_task_student` VALUES (424, 20211200596, 6, 78);
INSERT INTO `project_task_student` VALUES (425, 20211200596, 6, 50);
INSERT INTO `project_task_student` VALUES (426, 20211200596, 6, 76);
INSERT INTO `project_task_student` VALUES (427, 20211201458, 6, 77);
INSERT INTO `project_task_student` VALUES (428, 20211201458, 6, 78);
INSERT INTO `project_task_student` VALUES (429, 20211201458, 6, 48);
INSERT INTO `project_task_student` VALUES (430, 20211201458, 6, 76);
INSERT INTO `project_task_student` VALUES (431, 20211201903, 8, 69);
INSERT INTO `project_task_student` VALUES (432, 20211201903, 8, 71);
INSERT INTO `project_task_student` VALUES (433, 20211201903, 8, 75);
INSERT INTO `project_task_student` VALUES (434, 20211201785, 6, 77);
INSERT INTO `project_task_student` VALUES (435, 20211201785, 6, 78);
INSERT INTO `project_task_student` VALUES (436, 20211201785, 6, 49);
INSERT INTO `project_task_student` VALUES (437, 20211201785, 6, 76);

-- ----------------------------
-- Table structure for projects
-- ----------------------------
DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `projects_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '所有项目' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of projects
-- ----------------------------
INSERT INTO `projects` VALUES (1, '动态企业网站系统');
INSERT INTO `projects` VALUES (2, '物流管理系统');
INSERT INTO `projects` VALUES (3, '电影订票网站');
INSERT INTO `projects` VALUES (4, '团购网站');
INSERT INTO `projects` VALUES (5, '酒店预定管理系统');
INSERT INTO `projects` VALUES (6, '客户关系管理系统');
INSERT INTO `projects` VALUES (7, '网上订餐系统');
INSERT INTO `projects` VALUES (8, 'Web投稿及稿件处理系统');

-- ----------------------------
-- Table structure for sou_test
-- ----------------------------
DROP TABLE IF EXISTS `sou_test`;
CREATE TABLE `sou_test`  (
  `number` int NOT NULL,
  `stuid` bigint NULL DEFAULT NULL,
  `stuname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `stuclass` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k4` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k5` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `kt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s4` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s5` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `st` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `x1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `x2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `x3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pkt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `qm` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `k20` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `s20` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `x30` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `qmt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `total` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sou_test
-- ----------------------------
INSERT INTO `sou_test` VALUES (1, 20191202255, '纪嘉俊', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '0', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (2, 20201202139, '张子龙', '2021软件工程1班', '100', '60', '60', NULL, NULL, '44', NULL, NULL, NULL, NULL, NULL, '0', '0', '0', NULL, '0', NULL, '8.8', '0', '0', '0', '8.8');
INSERT INTO `sou_test` VALUES (3, 20211200384, '严芊芊', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '100', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (4, 20211200551, '曾繁一', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '80', NULL, '59.333333', NULL, '12', '0', '17.8', '0', '29.8');
INSERT INTO `sou_test` VALUES (5, 20211200556, '王鑫', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '90', NULL, '63.333333', NULL, '12', '0', '19', '0', '31');
INSERT INTO `sou_test` VALUES (6, 20211200558, '王贵萱', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '0', NULL, '35', NULL, '12', '0', '10.5', '0', '22.5');
INSERT INTO `sou_test` VALUES (7, 20211200584, '何彦莹', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '80', NULL, '59.333333', NULL, '12', '0', '17.8', '0', '29.8');
INSERT INTO `sou_test` VALUES (8, 20211200602, '刘鑫宇', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', '60', NULL, NULL, NULL, NULL, '12', '105', '-20', NULL, '28.333333', NULL, '12', '2.4', '8.5', '0', '22.9');
INSERT INTO `sou_test` VALUES (9, 20211200605, '郑琳', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '60', NULL, '52.666667', NULL, '12', '0', '15.8', '0', '27.8');
INSERT INTO `sou_test` VALUES (10, 20211200710, '汪康', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '0', NULL, '35', NULL, '12', '0', '10.5', '0', '22.5');
INSERT INTO `sou_test` VALUES (11, 20211200719, '王鹏', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '90', NULL, '62.666667', NULL, '12', '0', '18.8', '0', '30.8');
INSERT INTO `sou_test` VALUES (12, 20211201141, '闫政', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '90', NULL, '62.666667', NULL, '12', '0', '18.8', '0', '30.8');
INSERT INTO `sou_test` VALUES (13, 20211201148, '郭会发', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '40', NULL, '46', NULL, '12', '0', '13.8', '0', '25.8');
INSERT INTO `sou_test` VALUES (14, 20211201392, '孙可言', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (15, 20211201418, '刘陵', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '80', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (16, 20211201458, '焦海霞', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (17, 20211201483, '张含锋', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '100', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (18, 20211201803, '张士博', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '0', NULL, '33.333333', NULL, '12', '0', '10', '0', '22');
INSERT INTO `sou_test` VALUES (19, 20211201804, '葛怀睿', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '109', '0', NULL, '36.333333', NULL, '12', '0', '10.9', '0', '22.9');
INSERT INTO `sou_test` VALUES (20, 20211201806, '刘帅博', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '50', NULL, '46.666667', NULL, '12', '0', '14', '0', '26');
INSERT INTO `sou_test` VALUES (21, 20211201849, '魏继瑶', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '50', NULL, '49.333333', NULL, '12', '0', '14.8', '0', '26.8');
INSERT INTO `sou_test` VALUES (22, 20211201874, '郭伟康', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '-20', NULL, '26.666667', NULL, '12', '0', '8', '0', '20');
INSERT INTO `sou_test` VALUES (23, 20211201875, '王林超', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', '60', NULL, NULL, NULL, NULL, '12', '60', '0', NULL, '20', NULL, '12', '2.4', '6', '0', '20.4');
INSERT INTO `sou_test` VALUES (24, 20211201878, '杨嘉沐', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (25, 20211201897, '张锐颀', '2021软件工程1班', '100', '100', '95', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '90', '90', NULL, '60', NULL, '11.8', '0', '18', '0', '29.8');
INSERT INTO `sou_test` VALUES (26, 20211201899, '刘子轩', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (27, 20211201903, '董美娇', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (28, 20211202068, '常松', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '90', NULL, '60', NULL, '12', '0', '18', '0', '30');
INSERT INTO `sou_test` VALUES (29, 20211202073, '陈浩然', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '0', NULL, '33.333333', NULL, '12', '0', '10', '0', '22');
INSERT INTO `sou_test` VALUES (30, 20211202083, '高铎', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '50', NULL, '49.333333', NULL, '12', '0', '14.8', '0', '26.8');
INSERT INTO `sou_test` VALUES (31, 20211202101, '陈广硕', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '0', NULL, '35', NULL, '12', '0', '10.5', '0', '22.5');
INSERT INTO `sou_test` VALUES (32, 20211202103, '张瑛琪', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '0', NULL, '35', NULL, '12', '0', '10.5', '0', '22.5');
INSERT INTO `sou_test` VALUES (33, 20211202111, '张博', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (34, 20211202125, '黄照凯', '2021软件工程1班', '100', '100', '90', NULL, NULL, '58', NULL, NULL, NULL, NULL, NULL, '0', '105', '50', NULL, '51.666667', NULL, '11.6', '0', '15.5', '0', '27.1');
INSERT INTO `sou_test` VALUES (35, 20211202326, '李俊兰', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (36, 20211202380, '李轩', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '40', NULL, '46.666667', NULL, '12', '0', '14', '0', '26');
INSERT INTO `sou_test` VALUES (37, 20211202495, '饶峰', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '96', '80', NULL, '58.666667', NULL, '12', '0', '17.6', '0', '29.6');
INSERT INTO `sou_test` VALUES (38, 20211202543, '罗民富', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '97', '-30', NULL, '22.333333', NULL, '12', '0', '6.7', '0', '18.7');
INSERT INTO `sou_test` VALUES (39, 20211202705, '丁金洋', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '0', NULL, '32.666667', NULL, '12', '0', '9.8', '0', '21.8');
INSERT INTO `sou_test` VALUES (40, 20211202723, '田兆卓', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (41, 20211202724, '王洪福', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (42, 20211202759, '唐文勃', '2021软件工程1班', '100', '100', '95', NULL, NULL, '59', '60', NULL, NULL, NULL, NULL, '12', '100', '0', NULL, '33.333333', NULL, '11.8', '2.4', '10', '0', '24.2');
INSERT INTO `sou_test` VALUES (43, 20211202868, '孙艺慧', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '90', NULL, '63.333333', NULL, '12', '0', '19', '0', '31');
INSERT INTO `sou_test` VALUES (44, 20211202878, '涂泉源', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '100', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (45, 20211202900, '陈梦飞', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '70', NULL, '56.666667', NULL, '12', '0', '17', '0', '29');
INSERT INTO `sou_test` VALUES (46, 20211203012, '王冠涵', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '-10', NULL, '30', NULL, '12', '0', '9', '0', '21');
INSERT INTO `sou_test` VALUES (47, 20211203035, '卢平', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '90', NULL, '62.666667', NULL, '12', '0', '18.8', '0', '30.8');
INSERT INTO `sou_test` VALUES (48, 20211203038, '刘浩宇', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (49, 20211203049, '尹春普', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '98', '80', NULL, '59.333333', NULL, '12', '0', '17.8', '0', '29.8');
INSERT INTO `sou_test` VALUES (50, 20211203783, '张楠', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '0', NULL, '33.333333', NULL, '12', '0', '10', '0', '22');
INSERT INTO `sou_test` VALUES (51, 20211203980, '刘佳欣', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '100', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (52, 20211203983, '郑久彤', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '60', NULL, '55', NULL, '12', '0', '16.5', '0', '28.5');
INSERT INTO `sou_test` VALUES (53, 20211204314, '阮龙', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (54, 20211204412, '唐韧', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (55, 20211204414, '周作友', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '-30', NULL, '20', NULL, '12', '0', '6', '0', '18');
INSERT INTO `sou_test` VALUES (56, 20211204954, '张溪桐', '2021软件工程1班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '50', NULL, '46.666667', NULL, '12', '0', '14', '0', '26');
INSERT INTO `sou_test` VALUES (57, 20181203922, '王子康', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '60', '0', NULL, '20', NULL, '12', '0', '6', '0', '18');
INSERT INTO `sou_test` VALUES (58, 20191202610, '段兴江', '2021软件工程2班', '100', '60', '60', NULL, NULL, '44', NULL, NULL, NULL, NULL, NULL, '0', '90', '-10', NULL, '26.666667', NULL, '8.8', '0', '8', '0', '16.8');
INSERT INTO `sou_test` VALUES (59, 20211200385, '顾培皓', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '75', '-40', NULL, '11.666667', NULL, '12', '0', '3.5', '0', '15.5');
INSERT INTO `sou_test` VALUES (60, 20211200553, '王宗祥', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '70', NULL, '53.333333', NULL, '12', '0', '16', '0', '28');
INSERT INTO `sou_test` VALUES (61, 20211200596, '于舒睿', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '85', '0', NULL, '28.333333', NULL, '12', '0', '8.5', '0', '20.5');
INSERT INTO `sou_test` VALUES (62, 20211200598, '张杨', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-7', '0', NULL, '-2.333333', NULL, '12', '0', '-0.7', '0', '11.3');
INSERT INTO `sou_test` VALUES (63, 20211200601, '孙欣欣', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', NULL, '-40', NULL, '-13.333333', NULL, '12', '0', '-4', '0', '8');
INSERT INTO `sou_test` VALUES (64, 20211200606, '迟稼铭', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-10', '0', NULL, '-3.333333', NULL, '12', '0', '-1', '0', '11');
INSERT INTO `sou_test` VALUES (65, 20211200711, '章嘉劭', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '93', '50', NULL, '47.666667', NULL, '12', '0', '14.3', '0', '26.3');
INSERT INTO `sou_test` VALUES (66, 20211201119, '王福龙', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '80', '70', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (67, 20211201454, '何海兴', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '93', '60', NULL, '51', NULL, '12', '0', '15.3', '0', '27.3');
INSERT INTO `sou_test` VALUES (68, 20211201457, '赵旋', '2021软件工程2班', '100', '95', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '105', '50', NULL, '51.666667', NULL, '11.8', '0', '15.5', '0', '27.3');
INSERT INTO `sou_test` VALUES (69, 20211201659, '彭锦龙', '2021软件工程2班', '100', '100', '95', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '60', '0', NULL, '20', NULL, '11.8', '0', '6', '0', '17.8');
INSERT INTO `sou_test` VALUES (70, 20211201766, '李欣欢', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '70', NULL, '53.333333', NULL, '12', '0', '16', '0', '28');
INSERT INTO `sou_test` VALUES (71, 20211201785, '马乐晨', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '0', NULL, '30', NULL, '12', '0', '9', '0', '21');
INSERT INTO `sou_test` VALUES (72, 20211201793, '乔佳昕', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '93', '0', NULL, '31', NULL, '12', '0', '9.3', '0', '21.3');
INSERT INTO `sou_test` VALUES (73, 20211201867, '付陈瑶', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '60', '90', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (74, 20211201890, '常宏伟', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '80', NULL, '63.333333', NULL, '12', '0', '19', '0', '31');
INSERT INTO `sou_test` VALUES (75, 20211201893, '韩森宇', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '90', NULL, '60', NULL, '12', '0', '18', '0', '30');
INSERT INTO `sou_test` VALUES (76, 20211201900, '王腾鑫', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '90', NULL, '60', NULL, '12', '0', '18', '0', '30');
INSERT INTO `sou_test` VALUES (77, 20211201902, '张睿泽', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-5', '-40', NULL, '-15', NULL, '12', '0', '-4.5', '0', '7.5');
INSERT INTO `sou_test` VALUES (78, 20211202069, '刘庆龙', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '80', '-10', NULL, '23.333333', NULL, '12', '0', '7', '0', '19');
INSERT INTO `sou_test` VALUES (79, 20211202072, '邢子阳', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '60', '0', NULL, '20', NULL, '12', '0', '6', '0', '18');
INSERT INTO `sou_test` VALUES (80, 20211202079, '祁明扬', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (81, 20211202081, '任靓', '2021软件工程2班', '100', '100', '95', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '95', '75', NULL, '56.666667', NULL, '11.8', '0', '17', '0', '28.8');
INSERT INTO `sou_test` VALUES (82, 20211202090, '姚祥桐', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '110', NULL, '68.333333', NULL, '12', '0', '20.5', '0', '32.5');
INSERT INTO `sou_test` VALUES (83, 20211202095, '王雅鑫', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '0', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (84, 20211202104, '耿唯瀚', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '80', '0', NULL, '26.666667', NULL, '12', '0', '8', '0', '20');
INSERT INTO `sou_test` VALUES (85, 20211202112, '李明哲', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '85', '-40', NULL, '15', NULL, '12', '0', '4.5', '0', '16.5');
INSERT INTO `sou_test` VALUES (86, 20211202312, '徐婷', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '0', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (87, 20211202355, '支毅博', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '75', '-20', NULL, '18.333333', NULL, '12', '0', '5.5', '0', '17.5');
INSERT INTO `sou_test` VALUES (88, 20211202362, '赵佳乐', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '60', '0', NULL, '20', NULL, '12', '0', '6', '0', '18');
INSERT INTO `sou_test` VALUES (89, 20211202487, '翟翱', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '0', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (90, 20211202720, '张书通', '2021软件工程2班', '100', '100', '90', NULL, NULL, '58', NULL, NULL, NULL, NULL, NULL, '0', '90', '-40', NULL, '16.666667', NULL, '11.6', '0', '5', '0', '16.6');
INSERT INTO `sou_test` VALUES (91, 20211202726, '李韩', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '80', '70', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (92, 20211202730, '郭桐羽', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-20', '0', NULL, '-6.666667', NULL, '12', '0', '-2', '0', '10');
INSERT INTO `sou_test` VALUES (93, 20211202732, '张宇', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '85', '90', NULL, '58.333333', NULL, '12', '0', '17.5', '0', '29.5');
INSERT INTO `sou_test` VALUES (94, 20211202744, '王祉桥', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-20', NULL, '30', NULL, '12', '0', '9', '0', '21');
INSERT INTO `sou_test` VALUES (95, 20211202754, '刘扬', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-10', '-35', NULL, '-15', NULL, '12', '0', '-4.5', '0', '7.5');
INSERT INTO `sou_test` VALUES (96, 20211202822, '何通海', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '60', NULL, '51.666667', NULL, '12', '0', '15.5', '0', '27.5');
INSERT INTO `sou_test` VALUES (97, 20211202855, '任子豪', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '60', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (98, 20211202881, '吴健南', '2021软件工程2班', '100', '100', '95', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '85', '110', NULL, '65', NULL, '11.8', '0', '19.5', '0', '31.3');
INSERT INTO `sou_test` VALUES (99, 20211202947, '许孙凯', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '110', NULL, '68.333333', NULL, '12', '0', '20.5', '0', '32.5');
INSERT INTO `sou_test` VALUES (100, 20211202948, '白明涛', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '110', NULL, '68.333333', NULL, '12', '0', '20.5', '0', '32.5');
INSERT INTO `sou_test` VALUES (101, 20211203042, '信帅权', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '60', '-20', NULL, '13.333333', NULL, '12', '0', '4', '0', '16');
INSERT INTO `sou_test` VALUES (102, 20211203047, '邓大卫', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '80', NULL, '63.333333', NULL, '12', '0', '19', '0', '31');
INSERT INTO `sou_test` VALUES (103, 20211203059, '刘思豪', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '93', '0', NULL, '31', NULL, '12', '0', '9.3', '0', '21.3');
INSERT INTO `sou_test` VALUES (104, 20211203089, '张义超', '2021软件工程2班', '100', '67', '0', NULL, NULL, '33.4', NULL, NULL, NULL, NULL, NULL, '0', '60', '-15', NULL, '15', NULL, '6.68', '0', '4.5', '0', '11.18');
INSERT INTO `sou_test` VALUES (105, 20211203091, '王格格', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (106, 20211203792, '戴明东', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '90', '90', NULL, '60', NULL, '12', '0', '18', '0', '30');
INSERT INTO `sou_test` VALUES (107, 20211203974, '李涵', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '50', NULL, '53.333333', NULL, '12', '0', '16', '0', '28');
INSERT INTO `sou_test` VALUES (108, 20211203978, '栾凯越', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '85', '60', NULL, '48.333333', NULL, '12', '0', '14.5', '0', '26.5');
INSERT INTO `sou_test` VALUES (109, 20211203986, '崔惟桓', '2021软件工程2班', '100', '0', '67', NULL, NULL, '33.4', NULL, NULL, NULL, NULL, NULL, '0', '-10', '-35', NULL, '-15', NULL, '6.68', '0', '-4.5', '0', '2.18');
INSERT INTO `sou_test` VALUES (110, 20211203987, '刘晨阳', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-10', '-40', NULL, '-16.666667', NULL, '12', '0', '-5', '0', '7');
INSERT INTO `sou_test` VALUES (111, 20211203994, '吴航宇', '2021软件工程2班', '0', '0', '33', NULL, NULL, '6.6', NULL, NULL, NULL, NULL, NULL, '0', '-10', '70', NULL, '20', NULL, '1.32', '0', '6', '0', '7.32');
INSERT INTO `sou_test` VALUES (112, 20211203996, '夏单祁', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '110', NULL, '68.333333', NULL, '12', '0', '20.5', '0', '32.5');
INSERT INTO `sou_test` VALUES (113, 20211204434, '尹才华', '2021软件工程2班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '-10', '0', NULL, '-3.333333', NULL, '12', '0', '-1', '0', '11');
INSERT INTO `sou_test` VALUES (114, 20212200919, '何玉', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '75', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (115, 20212200989, '袁晓淋', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '60', NULL, '55', NULL, '12', '0', '16.5', '0', '28.5');
INSERT INTO `sou_test` VALUES (116, 20212201080, '曹祝群', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '90', NULL, '65', NULL, '12', '0', '19.5', '0', '31.5');
INSERT INTO `sou_test` VALUES (117, 20212201098, '陈前', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '20', NULL, '41.666667', NULL, '12', '0', '12.5', '0', '24.5');
INSERT INTO `sou_test` VALUES (118, 20212201146, '杨承璐', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '80', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (119, 20212201172, '龚相涛', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '-30', NULL, '21.666667', NULL, '12', '0', '6.5', '0', '18.5');
INSERT INTO `sou_test` VALUES (120, 20212201251, '王志远', '2021软件工程3班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '105', '80', NULL, '61.666667', NULL, '11.8', '0', '18.5', '0', '30.3');
INSERT INTO `sou_test` VALUES (121, 20212201258, '张玉钦', '2021软件工程3班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '90', '0', NULL, '30', NULL, '11.8', '0', '9', '0', '20.8');
INSERT INTO `sou_test` VALUES (122, 20212201310, '王藜璇', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '20', NULL, '41.666667', NULL, '12', '0', '12.5', '0', '24.5');
INSERT INTO `sou_test` VALUES (123, 20212201320, '张涛', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '0', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (124, 20212201324, '郑俊', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '95', '-10', NULL, '28.333333', NULL, '12', '0', '8.5', '0', '20.5');
INSERT INTO `sou_test` VALUES (125, 20212201330, '李正梅', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '0', NULL, '33.333333', NULL, '12', '0', '10', '0', '22');
INSERT INTO `sou_test` VALUES (126, 20212201335, '武丽', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '60', NULL, '53.333333', NULL, '12', '0', '16', '0', '28');
INSERT INTO `sou_test` VALUES (127, 20212201350, '罗亚婷', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (128, 20212201351, '张文瑞', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '75', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (129, 20212201360, '邹洪东', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '40', NULL, '48.333333', NULL, '12', '0', '14.5', '0', '26.5');
INSERT INTO `sou_test` VALUES (130, 20212201365, '孟维', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '50', NULL, '50', NULL, '12', '0', '15', '0', '27');
INSERT INTO `sou_test` VALUES (131, 20212201370, '施嘉鋆', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '0', NULL, '33.333333', NULL, '12', '0', '10', '0', '22');
INSERT INTO `sou_test` VALUES (132, 20212201373, '段周清', '2021软件工程3班', '100', '95', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '11.8', '0', '9.5', '0', '21.3');
INSERT INTO `sou_test` VALUES (133, 20212201382, '段丽萍', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '-20', NULL, '26.666667', NULL, '12', '0', '8', '0', '20');
INSERT INTO `sou_test` VALUES (134, 20212201391, '杨周成', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (135, 20212201393, '张文腾', '2021软件工程3班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '110', '100', NULL, '70', NULL, '11.8', '0', '21', '0', '32.8');
INSERT INTO `sou_test` VALUES (136, 20212201399, '郑洁', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '20', NULL, '41.666667', NULL, '12', '0', '12.5', '0', '24.5');
INSERT INTO `sou_test` VALUES (137, 20212201401, '徐艺', '2021软件工程3班', '100', '95', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '11.8', '0', '9.5', '0', '21.3');
INSERT INTO `sou_test` VALUES (138, 20212201402, '伍吉红', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '80', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (139, 20212201403, '顾敬文', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '75', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (140, 20212201404, '吴水仙', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '75', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (141, 20212201408, '张运', '2021软件工程3班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '105', '40', NULL, '48.333333', NULL, '11.8', '0', '14.5', '0', '26.3');
INSERT INTO `sou_test` VALUES (142, 20212201409, '姜人靖', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (143, 20212201417, '陈寿富', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-15', NULL, '31.666667', NULL, '12', '0', '9.5', '0', '21.5');
INSERT INTO `sou_test` VALUES (144, 20212201423, '陈玉华', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '75', NULL, '61.666667', NULL, '12', '0', '18.5', '0', '30.5');
INSERT INTO `sou_test` VALUES (145, 20212201434, '龚礼东', '2021软件工程3班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '11.8', '0', '22', '0', '33.8');
INSERT INTO `sou_test` VALUES (146, 20212201435, '杨宏发', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '-20', NULL, '26.666667', NULL, '12', '0', '8', '0', '20');
INSERT INTO `sou_test` VALUES (147, 20212201436, '余晨', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '100', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (148, 20212201448, '李瞵昌', '2021软件工程3班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '105', '60', NULL, '55', NULL, '12', '0', '16.5', '0', '28.5');
INSERT INTO `sou_test` VALUES (149, 20212200937, '何紫萱', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '110', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (150, 20212200947, '梁雷', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (151, 20212201128, '吕茂奎', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (152, 20212201192, '杨大鹏', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (153, 20212201227, '李有英', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (154, 20212201312, '蔡昊洋', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-40', NULL, '23.333333', NULL, '12', '0', '7', '0', '19');
INSERT INTO `sou_test` VALUES (155, 20212201313, '赵润萍', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '90', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (156, 20212201315, '王茂', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (157, 20212201321, '李明坤', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (158, 20212201323, '廖雅杰', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '90', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (159, 20212201326, '张宇', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (160, 20212201331, '邓信松', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '90', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (161, 20212201336, '欧阳进懿', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (162, 20212201340, '李天建', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (163, 20212201347, '刘沅超', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '110', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (164, 20212201355, '王福禄', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '110', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (165, 20212201359, '张永丽', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '25', NULL, '45', NULL, '12', '0', '13.5', '0', '25.5');
INSERT INTO `sou_test` VALUES (166, 20212201366, '陈应仙', '2021软件工程4班', '90', '100', '100', NULL, NULL, '58', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '11.6', '0', '22', '0', '33.6');
INSERT INTO `sou_test` VALUES (167, 20212201367, '杨杨', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (168, 20212201369, '杨柠柠', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '25', NULL, '45', NULL, '12', '0', '13.5', '0', '25.5');
INSERT INTO `sou_test` VALUES (169, 20212201380, '亚比生', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (170, 20212201385, '贾栋凯', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (171, 20212201392, '罗成亮', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (172, 20212201394, '马露优', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '110', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (173, 20212201397, '王劲尧', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '90', NULL, '66.666667', NULL, '12', '0', '20', '0', '32');
INSERT INTO `sou_test` VALUES (174, 20212201400, '马明静', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '80', '110', NULL, '63.333333', NULL, '12', '0', '19', '0', '31');
INSERT INTO `sou_test` VALUES (175, 20212201405, '龚琛', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '-40', NULL, '23.333333', NULL, '12', '0', '7', '0', '19');
INSERT INTO `sou_test` VALUES (176, 20212201410, '黄荣多', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '25', NULL, '45', NULL, '12', '0', '13.5', '0', '25.5');
INSERT INTO `sou_test` VALUES (177, 20212201413, '李强贵', '2021软件工程4班', '95', '100', '100', NULL, NULL, '59', NULL, NULL, NULL, NULL, NULL, '0', '95', '110', NULL, '68.333333', NULL, '11.8', '0', '20.5', '0', '32.3');
INSERT INTO `sou_test` VALUES (178, 20212201414, '王晓敏', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '0', NULL, '36.666667', NULL, '12', '0', '11', '0', '23');
INSERT INTO `sou_test` VALUES (179, 20212201420, '卢仕韦', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (180, 20212201439, '赵昌粉', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '100', '110', NULL, '70', NULL, '12', '0', '21', '0', '33');
INSERT INTO `sou_test` VALUES (181, 20212201441, '茶炳榕', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '110', NULL, '73.333333', NULL, '12', '0', '22', '0', '34');
INSERT INTO `sou_test` VALUES (182, 20212201446, '余书艳', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '25', NULL, '45', NULL, '12', '0', '13.5', '0', '25.5');
INSERT INTO `sou_test` VALUES (183, 20212201449, '张清远', '2021软件工程4班', '100', '100', '100', NULL, NULL, '60', NULL, NULL, NULL, NULL, NULL, '0', '110', '25', NULL, '45', NULL, '12', '0', '13.5', '0', '25.5');

-- ----------------------------
-- Table structure for student_info
-- ----------------------------
DROP TABLE IF EXISTS `student_info`;
CREATE TABLE `student_info`  (
  `stu_number` int NULL DEFAULT NULL COMMENT '学生序号',
  `stu_id` bigint NOT NULL COMMENT '学生学号',
  `stu_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `stu_class` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生班级',
  `project_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目地址',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '学生信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_info
-- ----------------------------
INSERT INTO `student_info` VALUES (10, 2021120710, '汪康', '软件工程1班', '');
INSERT INTO `student_info` VALUES (1, 20181203922, '王子康', '软件工程2班', 'http://47.115.220.55:8086/news');
INSERT INTO `student_info` VALUES (1, 20191202255, '纪嘉俊', '软件工程1班', 'http://47.120.52.41:8086');
INSERT INTO `student_info` VALUES (2, 20191202610, '段兴江', '软件工程2班', 'http://47.120.50.159:8086/hoteldetall');
INSERT INTO `student_info` VALUES (2, 20201202139, '张子龙', '软件工程1班', 'https://www.baidu.com');
INSERT INTO `student_info` VALUES (3, 20211200384, '严芊芊', '软件工程1班', 'http://47.115.211.43:8086/le-balance.html');
INSERT INTO `student_info` VALUES (3, 20211200385, '顾培皓', '软件工程2班', 'http://47.120.0.239:8086/htmlindex');
INSERT INTO `student_info` VALUES (4, 20211200551, '曾繁一', '软件工程1班', 'http://47.120.50.99:8086/index');
INSERT INTO `student_info` VALUES (4, 20211200553, '王宗祥', '软件工程2班', 'http://47.115.220.55:8086');
INSERT INTO `student_info` VALUES (5, 20211200556, '王鑫', '软件工程1班', 'http://47.120.53.164:8086/Order.html');
INSERT INTO `student_info` VALUES (6, 20211200558, '王贵萱', '软件工程1班', 'http://47.120.53.233:8119/olist');
INSERT INTO `student_info` VALUES (7, 20211200584, '何彦莹', '软件工程1班', 'http://47.120.53.233:8119/');
INSERT INTO `student_info` VALUES (5, 20211200596, '于舒睿', '软件工程2班', 'http://47.120.51.202:8086/sale/saleList');
INSERT INTO `student_info` VALUES (6, 20211200598, '张杨', '软件工程2班', 'http://47.120.0.239:8086/api1/products');
INSERT INTO `student_info` VALUES (7, 20211200601, '孙欣欣', '软件工程2班', 'http://47.120.0.239:8086/comment/ulist');
INSERT INTO `student_info` VALUES (8, 20211200602, '刘鑫宇', '软件工程1班', 'http://47.120.53.233:8119/');
INSERT INTO `student_info` VALUES (9, 20211200605, '郑琳', '软件工程1班', 'http://47.120.51.242:8086/dlist');
INSERT INTO `student_info` VALUES (8, 20211200606, '迟稼铭', '软件工程2班', '');
INSERT INTO `student_info` VALUES (9, 20211200711, '章嘉劭', '软件工程2班', 'http://47.120.0.239:8086/login');
INSERT INTO `student_info` VALUES (11, 20211200719, '王鹏', '软件工程1班', 'http://47.120.51.242:8086/glist');
INSERT INTO `student_info` VALUES (10, 20211201119, '王福龙', '软件工程2班', 'http://8.130.105.142:8086/clist');
INSERT INTO `student_info` VALUES (12, 20211201141, '闫政', '软件工程1班', 'http://8.137.70.184:8086/mlist');
INSERT INTO `student_info` VALUES (13, 20211201148, '郭会发', '软件工程1班', 'http://8.137.70.184:8086/ulist');
INSERT INTO `student_info` VALUES (14, 20211201392, '孙可言', '软件工程1班', 'http://8.130.41.58/le-return.html');
INSERT INTO `student_info` VALUES (15, 20211201418, '刘陵', '软件工程1班', 'http://47.120.53.233:8119/hlist');
INSERT INTO `student_info` VALUES (11, 20211201454, '何海兴', '软件工程2班', 'http://47.120.0.239/account/ulist');
INSERT INTO `student_info` VALUES (12, 20211201457, '赵旋', '软件工程2班', 'http://47.120.11.236:8086/plist');
INSERT INTO `student_info` VALUES (16, 20211201458, '焦海霞', '软件工程1班', 'http://47.120.12.198:8086/jhxlogin');
INSERT INTO `student_info` VALUES (17, 20211201483, '张含锋', '软件工程1班', 'http://47.120.37.15:8086/');
INSERT INTO `student_info` VALUES (13, 20211201659, '彭锦龙', '软件工程2班', 'http://8.130.105.142:8086/userOrder');
INSERT INTO `student_info` VALUES (14, 20211201766, '李欣欢', '软件工程2班', 'http://47.115.220.55:8086');
INSERT INTO `student_info` VALUES (15, 20211201785, '马乐晨', '软件工程2班', 'http://47.120.55.114:8086/');
INSERT INTO `student_info` VALUES (16, 20211201793, '乔佳昕', '软件工程2班', 'http://47.120.0.239:8086/clist');
INSERT INTO `student_info` VALUES (18, 20211201803, '张士博', '软件工程1班', 'http://39.105.138.43');
INSERT INTO `student_info` VALUES (19, 20211201804, '葛怀睿', '软件工程1班', 'http://47.120.51.242:8086/index');
INSERT INTO `student_info` VALUES (20, 20211201806, '刘帅博', '软件工程1班', '');
INSERT INTO `student_info` VALUES (21, 20211201849, '魏继瑶', '软件工程1班', 'http://47.120.53.167:userList');
INSERT INTO `student_info` VALUES (17, 20211201867, '付陈瑶', '软件工程2班', 'http://47.120.50.119:8086/twoGroup/price');
INSERT INTO `student_info` VALUES (22, 20211201874, '郭伟康', '软件工程1班', 'http://8.137.93.222:8086/shop.html');
INSERT INTO `student_info` VALUES (18, 20211201890, '常宏伟', '软件工程2班', 'http://47.120.11.236:8086/flist');
INSERT INTO `student_info` VALUES (19, 20211201893, '韩森宇', '软件工程2班', 'http://47.120.50.119:8086/twoGroup/userinfo/userinfo');
INSERT INTO `student_info` VALUES (25, 20211201897, '张锐颀', '软件工程1班', 'http://8.137.70.184:8086/');
INSERT INTO `student_info` VALUES (26, 20211201899, '刘子轩', '软件工程1班', 'http://39.106.73.179:8086/contract/list');
INSERT INTO `student_info` VALUES (20, 20211201900, '王腾鑫', '软件工程2班', 'http://47.120.50.119:8086/toGoodsHome');
INSERT INTO `student_info` VALUES (21, 20211201902, '张睿泽', '软件工程2班', 'http://47.120.50.159:8086/');
INSERT INTO `student_info` VALUES (27, 20211201903, '董美娇', '软件工程1班', 'http://47.120.50.210/ticket/Ticket');
INSERT INTO `student_info` VALUES (28, 20211202068, '常松', '软件工程1班', 'http://8.137.70.184:8086/listDispatch');
INSERT INTO `student_info` VALUES (22, 20211202069, '刘庆龙', '软件工程2班', '');
INSERT INTO `student_info` VALUES (23, 20211202072, '邢子阳', '软件工程2班', 'http://47.120.54.62:8086/vip');
INSERT INTO `student_info` VALUES (29, 20211202073, '陈浩然', '软件工程1班', 'http://8.137.70.184:8086/zlist');
INSERT INTO `student_info` VALUES (24, 20211202079, '祁明阳', '软件工程2班', 'http://47.120.11.236:8086/cinema');
INSERT INTO `student_info` VALUES (25, 20211202081, '任靓', '软件工程2班', 'http://47.120.54.10/list');
INSERT INTO `student_info` VALUES (30, 20211202083, '高铎', '软件工程1班', 'http://47.120.54.159:8086/userList');
INSERT INTO `student_info` VALUES (26, 20211202090, '姚祥桐', '软件工程2班', 'http://47.120.54.10:8086');
INSERT INTO `student_info` VALUES (27, 20211202095, '王雅鑫', '软件工程2班', 'http://47.120.50.159:8086/glist');
INSERT INTO `student_info` VALUES (31, 20211202101, '陈广硕', '软件工程1班', 'http://47.120.53.233:8119/blist');
INSERT INTO `student_info` VALUES (32, 20211202103, '张瑛琪', '软件工程1班', 'http://47.120.53.233:8119/alist');
INSERT INTO `student_info` VALUES (28, 20211202104, '耿唯瀚', '软件工程2班', '');
INSERT INTO `student_info` VALUES (33, 20211202111, '张博', '软件工程1班', 'http://8.130.125.38');
INSERT INTO `student_info` VALUES (29, 20211202112, '李明哲', '软件工程2班', 'http://47.115.220.55:8086/virtuosa/ulist');
INSERT INTO `student_info` VALUES (34, 20211202125, '黄照凯', '软件工程1班', 'http://47.120.53.233:8119/');
INSERT INTO `student_info` VALUES (30, 20211202312, '徐婷', '软件工程2班', 'http://47.120.50.159:8086/list');
INSERT INTO `student_info` VALUES (35, 20211202326, '李俊兰', '软件工程1班', 'http://47.120.50.104/ljlclist');
INSERT INTO `student_info` VALUES (31, 20211202355, '支毅博', '软件工程2班', 'http://8.130.105.142:8086/enroll');
INSERT INTO `student_info` VALUES (32, 20211202362, '赵佳乐', '软件工程2班', 'http://47.120.50.119:8086/dynamic');
INSERT INTO `student_info` VALUES (36, 20211202380, '李轩', '软件工程1班', 'http://47.120.53.58:8086/contract/list');
INSERT INTO `student_info` VALUES (33, 20211202487, '翟翱', '软件工程2班', 'http://47.120.50.159:8086/message');
INSERT INTO `student_info` VALUES (37, 20211202495, '饶峰', '软件工程1班', 'http://47.115.220.78/index');
INSERT INTO `student_info` VALUES (38, 20211202543, '罗民富', '软件工程1班', 'http://47.115.220.78/index');
INSERT INTO `student_info` VALUES (45, 20211202705, '丁金洋', '软件工程1班', 'http://47.120.54.152:8086');
INSERT INTO `student_info` VALUES (34, 20211202720, '张书通', '软件工程2班', 'http://47.115.220.55:8086/guanliyemian');
INSERT INTO `student_info` VALUES (40, 20211202723, '田兆卓', '软件工程1班', 'http://8.130.77.73:8086/');
INSERT INTO `student_info` VALUES (41, 20211202724, '王洪福', '软件工程1班', 'http://123.60.46.205:8086/glist');
INSERT INTO `student_info` VALUES (35, 20211202726, '李韩', '软件工程2班', 'http://8.130.105.142:8086/api/han');
INSERT INTO `student_info` VALUES (36, 20211202730, '郭桐羽', '软件工程2班', 'http://8.130.105.142:8086/waimai');
INSERT INTO `student_info` VALUES (37, 20211202732, '张宇', '软件工程2班', 'http://47.120.50.119:8086/twoGroup/settings');
INSERT INTO `student_info` VALUES (38, 20211202744, '王祉桥', '软件工程2班', 'http://47.120.11.236:8086/Movie_Schedule');
INSERT INTO `student_info` VALUES (39, 20211202754, '刘扬', '软件工程2班', 'http://47.115.220.55:8086/employee_managent');
INSERT INTO `student_info` VALUES (42, 20211202759, '唐文勃', '软件工程1班', 'http://8.137.70.184:8086/');
INSERT INTO `student_info` VALUES (40, 20211202822, '何通海', '软件工程2班', 'http://47.120.50.159:8086/hotelregister');
INSERT INTO `student_info` VALUES (41, 20211202855, '任子豪', '软件工程2班', 'http://47.120.50.159:8086/hotelindex');
INSERT INTO `student_info` VALUES (43, 20211202868, '孙艺慧', '软件工程1班', 'http://47.120.49.56:8086/customerList');
INSERT INTO `student_info` VALUES (44, 20211202878, '涂泉源', '软件工程1班', 'http://110.41.145.85:8086/');
INSERT INTO `student_info` VALUES (42, 20211202881, '吴健南', '软件工程2班', 'http://47.108.170.224/');
INSERT INTO `student_info` VALUES (45, 20211202900, '陈梦飞', '软件工程1班', 'http://8.130.85.164/test/register');
INSERT INTO `student_info` VALUES (43, 20211202947, '许孙凯', '软件工程2班', 'http://47.120.51.19/test_management');
INSERT INTO `student_info` VALUES (44, 20211202948, '白明涛', '软件工程2班', 'http://47.120.50.182:8086/index_login');
INSERT INTO `student_info` VALUES (46, 20211203012, '王冠涵', '软件工程1班', 'http://8.137.83.211:8086');
INSERT INTO `student_info` VALUES (47, 20211203035, '卢平', '软件工程1班', 'http://8.137.70.184:8086/v1/toGoodList');
INSERT INTO `student_info` VALUES (48, 20211203038, '刘浩宇', '软件工程1班', 'http://47.113.144.220:8086/mlist');
INSERT INTO `student_info` VALUES (45, 20211203042, '信帅权', '软件工程2班', 'http://8.130.105.142:8086/dishes/caidan');
INSERT INTO `student_info` VALUES (46, 20211203047, '邓大卫', '软件工程2班', 'http://47.120.11.236:8086/registry');
INSERT INTO `student_info` VALUES (49, 20211203049, '尹春普', '软件工程1班', 'http://47.115.220.78:8086/toCorporateWebsites');
INSERT INTO `student_info` VALUES (47, 20211203059, '刘思豪', '软件工程2班', 'http://47.120.0.239:8086/api/zhuce');
INSERT INTO `student_info` VALUES (48, 20211203089, '张义超', '软件工程2班', '');
INSERT INTO `student_info` VALUES (49, 20211203091, '王格格', '软件工程2班', 'http://47.120.11.236:8086/olist');
INSERT INTO `student_info` VALUES (50, 20211203783, '张楠', '软件工程1班', 'http://47.120.52.57:8086');
INSERT INTO `student_info` VALUES (50, 20211203792, '戴明东', '软件工程2班', 'http://47.120.50.119:8086/toStatement');
INSERT INTO `student_info` VALUES (51, 20211203974, '李涵', '软件工程2班', 'http://47.120.11.236:8086/shouye');
INSERT INTO `student_info` VALUES (52, 20211203978, '栾凯越', '软件工程2班', 'http://47.120.50.119:8086/Delivery');
INSERT INTO `student_info` VALUES (51, 20211203980, '刘佳欣', '软件工程1班', 'http://47.120.37.15:8086/');
INSERT INTO `student_info` VALUES (52, 20211203983, '郑久彤', '软件工程1班', 'http://8.130.125.38:8086/');
INSERT INTO `student_info` VALUES (53, 20211203986, '崔惟桓', '软件工程2班', '');
INSERT INTO `student_info` VALUES (54, 20211203987, '刘晨阳', '软件工程2班', 'http://47.115.220.55:8086/message');
INSERT INTO `student_info` VALUES (55, 20211203994, '吴航宇', '软件工程2班', 'http://47.115.220.55:8086/appointment');
INSERT INTO `student_info` VALUES (56, 20211203996, '夏单祁', '软件工程2班', 'http://47.113.199.30:8086');
INSERT INTO `student_info` VALUES (53, 20211204314, '阮龙', '软件工程1班', 'http://8.130.125.38:8086/');
INSERT INTO `student_info` VALUES (54, 20211204412, '唐韧', '软件工程1班', 'http://47.120.54.159:8086/contract/goStat');
INSERT INTO `student_info` VALUES (55, 20211204414, '周作友', '软件工程1班', 'http://http://47.120.38.179/8086');
INSERT INTO `student_info` VALUES (57, 20211204434, '尹才华', '软件工程2班', 'http://47.115.220.55:8086');
INSERT INTO `student_info` VALUES (56, 20211204954, '张溪桐', '软件工程1班', 'http://8.130.125.88/movie/ulist');
INSERT INTO `student_info` VALUES (1, 20212200919, '何玉', '软件工程3班', 'http://47.115.228.174/message.html');
INSERT INTO `student_info` VALUES (1, 20212200937, '何紫萱', '软件工程4班', 'http://47.113.188.102:8086/');
INSERT INTO `student_info` VALUES (2, 20212200947, '梁雷', '软件工程4班', 'http://47.120.49.84');
INSERT INTO `student_info` VALUES (2, 20212200989, '袁晓淋', '软件工程3班', 'http://47.120.55.112');
INSERT INTO `student_info` VALUES (3, 20212201080, '曹祝群', '软件工程3班', 'http://47.120.53.6/czq/index.html');
INSERT INTO `student_info` VALUES (4, 20212201098, '陈前', '软件工程3班', 'http://47.120.49.236:8080/');
INSERT INTO `student_info` VALUES (3, 20212201128, '吕茂奎', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/admin/dist/index.html');
INSERT INTO `student_info` VALUES (5, 20212201146, '杨承璐', '软件工程3班', 'http://47.120.54.2/indexdl.html');
INSERT INTO `student_info` VALUES (6, 20212201172, '龚相涛', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (4, 20212201192, '杨大鹏', '软件工程4班', 'http://47.97.154.144:8086/toAdmin');
INSERT INTO `student_info` VALUES (5, 20212201227, '李有英', '软件工程4班', 'http://47.97.154.144/selectXiang/5');
INSERT INTO `student_info` VALUES (8, 20212201251, '王志远', '软件工程3班', 'http://47.120.54.2/indexwzy.html');
INSERT INTO `student_info` VALUES (8, 20212201258, '张玉钦', '软件工程3班', 'http://47.120.54.134/');
INSERT INTO `student_info` VALUES (9, 20212201310, '王藜璇', '软件工程3班', '');
INSERT INTO `student_info` VALUES (6, 20212201312, '蔡昊洋', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/admin/dist/index.html');
INSERT INTO `student_info` VALUES (7, 20212201313, '赵润萍', '软件工程4班', 'https://orcspdm.icu/');
INSERT INTO `student_info` VALUES (8, 20212201315, '王茂', '软件工程4班', 'http://47.120.1.221:8086/goupiao?filmId=2');
INSERT INTO `student_info` VALUES (10, 20212201320, '张涛', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (9, 20212201321, '李明坤', '软件工程4班', 'http://47.97.154.144:8086/userlist');
INSERT INTO `student_info` VALUES (10, 20212201323, '廖雅杰', '软件工程4班', 'http://47.120.55.118');
INSERT INTO `student_info` VALUES (11, 20212201324, '郑俊', '软件工程3班', 'http://47.120.54.2/findDemoEntityList');
INSERT INTO `student_info` VALUES (11, 20212201326, '张宇', '软件工程4班', 'http://47.97.154.144:8086/toUserAdd');
INSERT INTO `student_info` VALUES (12, 20212201330, '李正梅', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (12, 20212201331, '邓信松', '软件工程4班', 'http://47.120.1.221:8086/root/admin');
INSERT INTO `student_info` VALUES (13, 20212201335, '武丽', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (13, 20212201336, '欧阳进懿', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/admin/dist/index.html');
INSERT INTO `student_info` VALUES (14, 20212201340, '李天建', '软件工程4班', 'http://litianjian.xyz');
INSERT INTO `student_info` VALUES (15, 20212201347, '刘沅超', '软件工程4班', 'http://47.120.12.114:8086/main');
INSERT INTO `student_info` VALUES (14, 20212201350, '罗亚婷', '软件工程3班', 'http://106.53.26.169/console/login');
INSERT INTO `student_info` VALUES (15, 20212201351, '张文瑞', '软件工程3班', 'http://47.115.228.174/room.html');
INSERT INTO `student_info` VALUES (16, 20212201355, '王福禄', '软件工程4班', 'http://47.120.51.32/main');
INSERT INTO `student_info` VALUES (17, 20212201359, '张永丽', '软件工程4班', 'https://orcspdm.icu/toDispatch');
INSERT INTO `student_info` VALUES (16, 20212201360, '邹洪东', '软件工程3班', '');
INSERT INTO `student_info` VALUES (17, 20212201365, '孟维', '软件工程3班', 'http://47.120.49.236:8080/login');
INSERT INTO `student_info` VALUES (18, 20212201366, '陈应仙', '软件工程4班', 'http://47.97.154.144:8086');
INSERT INTO `student_info` VALUES (19, 20212201367, '杨杨', '软件工程4班', 'http://8.137.124.53/');
INSERT INTO `student_info` VALUES (20, 20212201369, '杨柠柠', '软件工程4班', 'https://orcspdm.icu/');
INSERT INTO `student_info` VALUES (18, 20212201370, '施嘉鋆', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (19, 20212201373, '段周清', '软件工程3班', 'http://106.53.26.169/scheduleinquiry');
INSERT INTO `student_info` VALUES (21, 20212201380, '亚比生', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/admin/dist/index.html');
INSERT INTO `student_info` VALUES (20, 20212201382, '段丽萍', '软件工程3班', 'http://8.137.127.65:8086/main');
INSERT INTO `student_info` VALUES (22, 20212201385, '贾栋凯', '软件工程4班', 'http://47.120.1.221:8086/root/admin');
INSERT INTO `student_info` VALUES (21, 20212201391, '杨周成  ', '软件工程3班', 'http://106.53.26.169/buytickets');
INSERT INTO `student_info` VALUES (23, 20212201392, '罗成亮', '软件工程4班', 'http://47.120.1.221:8086');
INSERT INTO `student_info` VALUES (22, 20212201393, '张文腾', '软件工程3班', 'http://47.115.228.174/userUpdate.html');
INSERT INTO `student_info` VALUES (24, 20212201394, '马露优', '软件工程4班', 'http://47.120.54.230:8086/toUserss');
INSERT INTO `student_info` VALUES (25, 20212201397, '王劲尧', '软件工程4班', 'https://orcspdm.icu/');
INSERT INTO `student_info` VALUES (23, 20212201399, '郑洁', '软件工程3班', 'http://47.120.49.236:8080/admin/manage-recruitmentInfo');
INSERT INTO `student_info` VALUES (26, 20212201400, '马明静', '软件工程4班', 'http://47.120.54.230:8086');
INSERT INTO `student_info` VALUES (24, 20212201401, '徐艺', '软件工程3班', 'http://106.53.26.169/member');
INSERT INTO `student_info` VALUES (25, 20212201402, '伍吉红', '软件工程3班', 'http://47.120.54.2/indexdl.html');
INSERT INTO `student_info` VALUES (26, 20212201403, '顾敬文', '软件工程3班', 'http://47.115.228.174/accountManagement.html');
INSERT INTO `student_info` VALUES (27, 20212201404, '吴水仙', '软件工程3班', 'http://47.115.228.174:81/userUpdate.html');
INSERT INTO `student_info` VALUES (27, 20212201405, '龚琛', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/admin/dist/index.html');
INSERT INTO `student_info` VALUES (28, 20212201408, '张运', '软件工程3班', 'http://47.120.52.22/');
INSERT INTO `student_info` VALUES (29, 20212201409, '姜人靖', '软件工程3班', 'http://106.53.26.169/');
INSERT INTO `student_info` VALUES (28, 20212201410, '黄荣多', '软件工程4班', 'https://orcspdm.icu/');
INSERT INTO `student_info` VALUES (29, 20212201413, '李强贵', '软件工程4班', 'http://47.120.54.25/main');
INSERT INTO `student_info` VALUES (30, 20212201414, '王晓敏', '软件工程4班', 'http://47.120.54.33:8080/springbootjlvpC/front/index.html');
INSERT INTO `student_info` VALUES (30, 20212201417, '陈寿富', '软件工程3班', 'http://106.53.26.169/movieintroduction');
INSERT INTO `student_info` VALUES (31, 20212201420, '卢仕韦', '软件工程4班', 'http://47.120.53.94');
INSERT INTO `student_info` VALUES (31, 20212201423, '陈玉华', '软件工程3班', 'http://47.115.228.174/getting-start.html');
INSERT INTO `student_info` VALUES (32, 20212201434, '龚礼东', '软件工程3班', 'http://106.53.26.169/console/login');
INSERT INTO `student_info` VALUES (33, 20212201435, '杨宏发', '软件工程3班', 'http://8.137.127.65/main');
INSERT INTO `student_info` VALUES (34, 20212201436, '余晨', '软件工程3班', 'http://47.115.228.174/login.html');
INSERT INTO `student_info` VALUES (32, 20212201439, '赵昌粉', '软件工程4班', 'http://47.120.54.230:8086/main');
INSERT INTO `student_info` VALUES (33, 20212201441, '茶炳榕', '软件工程4班', 'http://47.120.50.78');
INSERT INTO `student_info` VALUES (34, 20212201446, '余书艳', '软件工程4班', 'https://orcspdm.icu/');
INSERT INTO `student_info` VALUES (35, 20212201448, '李瞵昌', '软件工程3班', 'http://47.120.54.2/trade.html');
INSERT INTO `student_info` VALUES (35, 20212201449, '张清远', '软件工程4班', 'https://orcspdm.icu/');

-- ----------------------------
-- Table structure for test_three
-- ----------------------------
DROP TABLE IF EXISTS `test_three`;
CREATE TABLE `test_three`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `x` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `y` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `z` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test_three
-- ----------------------------
INSERT INTO `test_three` VALUES (1, '2', '3', '4');
INSERT INTO `test_three` VALUES (2, '3', '4', '5');
INSERT INTO `test_three` VALUES (3, '4', '5', '6');
INSERT INTO `test_three` VALUES (4, 'hi', 'hello', 'sayj');
INSERT INTO `test_three` VALUES (5, '男', 'man', '1');

SET FOREIGN_KEY_CHECKS = 1;
