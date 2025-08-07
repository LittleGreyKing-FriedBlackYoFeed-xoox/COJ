/*
 Navicat Premium Data Transfer

 Source Server         : aliyun
 Source Server Type    : MySQL
 Source Server Version : 80028 (8.0.28)
 Source Host           : 47.109.155.118:3309
 Source Schema         : huihui

 Target Server Type    : MySQL
 Target Server Version : 80028 (8.0.28)
 File Encoding         : 65001

 Date: 08/03/2025 10:35:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for gonglidong_group_taskclassification
-- ----------------------------
DROP TABLE IF EXISTS `gonglidong_group_taskclassification`;
CREATE TABLE `gonglidong_group_taskclassification`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `leader_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '组长id',
  `leader_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '组长',
  `crew_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '组员id',
  `crew_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '组员',
  `task_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务id',
  `task_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务名称',
  `assignment_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务细则id',
  `assignment_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务细则名称',
  `assignment_content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务细则描述/介绍',
  `examine` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查方式',
  `taskstatus` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务状态',
  `executiontaskstatus` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '执行状态',
  `checksituation` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查情况',
  `fraction` double NULL DEFAULT NULL COMMENT '分数',
  `remark` varchar(700) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '备注',
  `isdel` tinyint NULL DEFAULT 0,
  `createtime` datetime NULL DEFAULT NULL,
  `updatetime` datetime NULL DEFAULT NULL,
  `deletetime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of gonglidong_group_taskclassification
-- ----------------------------
INSERT INTO `gonglidong_group_taskclassification` VALUES (1, '1', '李世辉', '', '马乐晨', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', '已完成', NULL, '', 0, '2024-04-24 18:50:30', '2024-04-24 18:50:30', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (2, '1', '李世辉', '', '耿唯瀚', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', '已完成', NULL, '', 0, '2024-04-24 18:50:47', '2024-04-24 18:50:47', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (3, '1', '李世辉', '', '于舒睿', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', '已完成', NULL, '', 0, '2024-04-24 18:50:55', '2024-04-24 18:50:55', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (4, '1', '李世辉', NULL, '迟稼铭', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (5, '1', '李世辉', NULL, '刘庆龙', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (6, '1', '李世辉', NULL, '刘扬', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 1, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (7, '1', '李世辉', NULL, '崔惟桓', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 1, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (8, '1', '李世辉', NULL, '唐文勃', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (9, '1', '李世辉', NULL, '王林超', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (10, '1', '李世辉', NULL, '张子龙', NULL, '①拉取huihui项目，项目地址：https://gitee.com/lijiang_lishihui/huihui.git\n②在4月15日之前完成5个CV请求并成功返回页面\n③书写一份CV请求过程总结报告，于15日提交', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '新分配', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (11, '1', '李世辉', NULL, '李天键', NULL, 'demo项目学生分数核查和细节修正', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '任务中', '执行中', NULL, NULL, NULL, 0, '2024-04-11 13:15:11', '2024-04-11 13:15:11', NULL);
INSERT INTO `gonglidong_group_taskclassification` VALUES (12, '1', '李世辉', '', '龚礼东', NULL, '任务分配表首页映射', NULL, NULL, NULL, '面检：15日当面完成CV请求案例', '紧急任务', '执行中', '已完成', NULL, '', 0, '2024-04-24 18:52:13', '2024-04-24 18:52:13', NULL);

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
) ENGINE = InnoDB AUTO_INCREMENT = 73 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '逻辑删去-默认是0，逻辑删去后标为1' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lishihui_system_user
-- ----------------------------
INSERT INTO `lishihui_system_user` VALUES (1, '小李', '124', '女', 10, '1111113', '丽江', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (2, 't', '123', '5', 21, '不要修改t用户', '不要修改t用户', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (4, '小张', '999999', '男', 10, '1851919198', '火星水星', '2020-10-16', '99@qq.com', 0, '2021-10-31 20:35:36', '2021-10-31 20:55:52', 1);
INSERT INTO `lishihui_system_user` VALUES (5, '小雪', '999999', '男', 20, '1851919198', '火星2', '2020-10-17', '99@qq.com', 1, '2021-10-31 20:35:36', '2021-10-31 20:35:36', 1);
INSERT INTO `lishihui_system_user` VALUES (6, '大李', '999999', '女', 21, '1881919879', '武汉', '2021-10-31', '99@qq.com', 0, '2021-10-31 20:40:13', '2021-10-31 20:40:13', 1);
INSERT INTO `lishihui_system_user` VALUES (22, '大李', NULL, '男', 29, '44058871', '丽江', NULL, NULL, 0, NULL, NULL, 1);
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
INSERT INTO `lishihui_system_user` VALUES (70, 'tt1', NULL, '女', 78, '44058871', '丽江', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (71, '张俊杰', '123', '男', 12, '15812341234', '中国', NULL, NULL, 0, NULL, NULL, 1);
INSERT INTO `lishihui_system_user` VALUES (72, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, 1);

-- ----------------------------
-- Table structure for pi
-- ----------------------------
DROP TABLE IF EXISTS `pi`;
CREATE TABLE `pi`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `orderName` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  `orderPrice` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of pi
-- ----------------------------
INSERT INTO `pi` VALUES (1, '鼠标', '120');
INSERT INTO `pi` VALUES (2, '键盘', '150');
INSERT INTO `pi` VALUES (3, '主板', '2000');

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task`  (
  `task_id` int NOT NULL AUTO_INCREMENT COMMENT '任务ID',
  `taskBeginTime` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '发布时间',
  `taskContent` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务内容',
  `inspectionMethods` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查方式',
  `inspectionTime` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查时间',
  `taskStatus` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '任务状态',
  `inspectors` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查人员',
  `InspectionSituation` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '检查情况',
  PRIMARY KEY (`task_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of task
-- ----------------------------
INSERT INTO `task` VALUES (1, '2024年4月11日', '完成5次MVC项目的CV请求', '面检', '2024年4月15日,00:00', '进行中', '李世辉', '待检查');
INSERT INTO `task` VALUES (2, '2024年4月11日', '拉取Gitee仓库中的项目并运行起来', '群内截图', '2024年4月12日，22:00', '已完成', '李世辉', '部分完成');
INSERT INTO `task` VALUES (3, '2024年4月12日', 'demo', NULL, NULL, NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
