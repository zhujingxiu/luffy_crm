-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018-10-26 08:18:34
-- 服务器版本： 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pycrm`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add 菜单管理', 7, 'add_menu'),
(20, 'Can change 菜单管理', 7, 'change_menu'),
(21, 'Can delete 菜单管理', 7, 'delete_menu'),
(22, 'Can add 权限节点', 8, 'add_permission'),
(23, 'Can change 权限节点', 8, 'change_permission'),
(24, 'Can delete 权限节点', 8, 'delete_permission'),
(25, 'Can add 角色管理', 9, 'add_role'),
(26, 'Can change 角色管理', 9, 'change_role'),
(27, 'Can delete 角色管理', 9, 'delete_role'),
(28, 'Can add 班级管理', 10, 'add_classinfo'),
(29, 'Can change 班级管理', 10, 'change_classinfo'),
(30, 'Can delete 班级管理', 10, 'delete_classinfo'),
(31, 'Can add 校区管理', 11, 'add_college'),
(32, 'Can change 校区管理', 11, 'change_college'),
(33, 'Can delete 校区管理', 11, 'delete_college'),
(34, 'Can add 课程管理', 12, 'add_course'),
(35, 'Can change 课程管理', 12, 'change_course'),
(36, 'Can delete 课程管理', 12, 'delete_course'),
(37, 'Can add 员工部门', 13, 'add_department'),
(38, 'Can change 员工部门', 13, 'change_department'),
(39, 'Can delete 员工部门', 13, 'delete_department'),
(40, 'Can add 员工账户', 14, 'add_userinfo'),
(41, 'Can change 员工账户', 14, 'change_userinfo'),
(42, 'Can delete 员工账户', 14, 'delete_userinfo'),
(43, 'Can add 转班记录', 15, 'add_changeclass'),
(44, 'Can change 转班记录', 15, 'change_changeclass'),
(45, 'Can delete 转班记录', 15, 'delete_changeclass'),
(46, 'Can add 客户跟进记录', 16, 'add_consultrecord'),
(47, 'Can change 客户跟进记录', 16, 'change_consultrecord'),
(48, 'Can delete 客户跟进记录', 16, 'delete_consultrecord'),
(49, 'Can add 上课记录', 17, 'add_courserecord'),
(50, 'Can change 上课记录', 17, 'change_courserecord'),
(51, 'Can delete 上课记录', 17, 'delete_courserecord'),
(52, 'Can add 客户管理', 18, 'add_customer'),
(53, 'Can change 客户管理', 18, 'change_customer'),
(54, 'Can delete 客户管理', 18, 'delete_customer'),
(55, 'Can add customer info', 19, 'add_customerinfo'),
(56, 'Can change customer info', 19, 'change_customerinfo'),
(57, 'Can delete customer info', 19, 'delete_customerinfo'),
(58, 'Can add 付款记录', 20, 'add_paymentrecord'),
(59, 'Can change 付款记录', 20, 'change_paymentrecord'),
(60, 'Can delete 付款记录', 20, 'delete_paymentrecord'),
(61, 'Can add 学员管理', 21, 'add_student'),
(62, 'Can change 学员管理', 21, 'change_student'),
(63, 'Can delete 学员管理', 21, 'delete_student'),
(64, 'Can add 学习记录', 22, 'add_studyrecord'),
(65, 'Can change 学习记录', 22, 'change_studyrecord'),
(66, 'Can delete 学习记录', 22, 'delete_studyrecord'),
(67, 'Can add 转班记录', 23, 'add_changerecord'),
(68, 'Can change 转班记录', 23, 'change_changerecord'),
(69, 'Can delete 转班记录', 23, 'delete_changerecord');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$5IVZsuurcOeu$JlNQoYcjGLtdCOJzxi1oPxlqyic5yFIZbZPoWGtoVI4=', NULL, 1, 'zhujingxiu', '', '', '', 1, 1, '2018-10-23 18:12:29.664849');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'rbac', 'menu'),
(8, 'rbac', 'permission'),
(9, 'rbac', 'role'),
(15, 'service', 'changeclass'),
(23, 'service', 'changerecord'),
(16, 'service', 'consultrecord'),
(17, 'service', 'courserecord'),
(18, 'service', 'customer'),
(19, 'service', 'customerinfo'),
(20, 'service', 'paymentrecord'),
(21, 'service', 'student'),
(22, 'service', 'studyrecord'),
(6, 'sessions', 'session'),
(10, 'system', 'classinfo'),
(11, 'system', 'college'),
(12, 'system', 'course'),
(13, 'system', 'department'),
(14, 'system', 'userinfo');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-10-23 18:11:21.033675'),
(2, 'auth', '0001_initial', '2018-10-23 18:11:28.303496'),
(3, 'admin', '0001_initial', '2018-10-23 18:11:29.640622'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-10-23 18:11:29.664909'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-10-23 18:11:30.493650'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-10-23 18:11:31.373950'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-10-23 18:11:32.166302'),
(8, 'auth', '0004_alter_user_username_opts', '2018-10-23 18:11:32.191593'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-10-23 18:11:32.603451'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-10-23 18:11:32.628410'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-10-23 18:11:32.663289'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-10-23 18:11:33.849035'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-10-23 18:11:34.408760'),
(14, 'rbac', '0001_initial', '2018-10-23 18:11:38.563681'),
(15, 'system', '0001_initial', '2018-10-23 18:11:48.836742'),
(17, 'sessions', '0001_initial', '2018-10-23 18:12:10.217560'),
(25, 'service', '0001_initial', '2018-10-24 19:23:17.899008'),
(26, 'service', '0002_auto_20181024_1558', '2018-10-24 19:23:17.945888'),
(27, 'service', '0003_auto_20181024_1833', '2018-10-24 19:23:17.981793'),
(28, 'service', '0004_changerecord', '2018-10-24 19:24:04.008255'),
(29, 'service', '0005_auto_20181024_1933', '2018-10-24 19:33:36.227866');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('l3nb4q1zv68adprbc8rwidaxvh082kui', 'OWFkMDhkMzhkMjYwMTI3NzcwZDRkNTBmOGVkMTJhODEyYmI1MWNiNzp7InhzdGFya19nZXQiOiJjY2lkPTEifQ==', '2018-11-08 16:13:38.935611');

-- --------------------------------------------------------

--
-- 表的结构 `rbac_menu`
--

CREATE TABLE `rbac_menu` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `icon` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `rbac_permission`
--

CREATE TABLE `rbac_permission` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `url` varchar(128) NOT NULL,
  `name` varchar(64) NOT NULL,
  `menu_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `rbac_role`
--

CREATE TABLE `rbac_role` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `code` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `rbac_role`
--

INSERT INTO `rbac_role` (`id`, `title`, `code`) VALUES
(1, '总监', 'master'),
(2, '讲师', 'teacher'),
(3, '销售', 'seller'),
(4, '客服', 'waiter'),
(5, '班主任', 'tutor');

-- --------------------------------------------------------

--
-- 表的结构 `rbac_role_permissions`
--

CREATE TABLE `rbac_role_permissions` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `service_changerecord`
--

CREATE TABLE `service_changerecord` (
  `id` int(11) NOT NULL,
  `memo` longtext NOT NULL,
  `add_date` datetime(6) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `origin_class_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `target_class_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `service_consultrecord`
--

CREATE TABLE `service_consultrecord` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `note` longtext NOT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_consultrecord`
--

INSERT INTO `service_consultrecord` (`id`, `date`, `note`, `consultant_id`, `customer_id`) VALUES
(1, '2018-10-25', 'qwewqeqwewq', 1, 1),
(2, '2018-10-25', '12321321321', 1, 2);

-- --------------------------------------------------------

--
-- 表的结构 `service_courserecord`
--

CREATE TABLE `service_courserecord` (
  `id` int(11) NOT NULL,
  `day_num` int(11) NOT NULL,
  `date` date NOT NULL,
  `course_title` varchar(64) DEFAULT NULL,
  `course_memo` longtext,
  `homework_title` varchar(64) NOT NULL,
  `homework_memo` longtext NOT NULL,
  `exam` longtext NOT NULL,
  `classinfo_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_courserecord`
--

INSERT INTO `service_courserecord` (`id`, `day_num`, `date`, `course_title`, `course_memo`, `homework_title`, `homework_memo`, `exam`, `classinfo_id`, `teacher_id`) VALUES
(1, 1, '2018-10-24', '12321321', '321321', '21321321', '12321', '21321', 1, 6),
(2, 1, '2018-10-25', '12321321', 'asdsadsa', 'as', 'asdsad', 'asd', 2, 6);

-- --------------------------------------------------------

--
-- 表的结构 `service_customer`
--

CREATE TABLE `service_customer` (
  `id` int(11) NOT NULL,
  `phone` varchar(32) NOT NULL,
  `sns` varchar(64) NOT NULL,
  `name` varchar(16) NOT NULL,
  `status` int(11) NOT NULL,
  `gender` smallint(6) NOT NULL,
  `source` smallint(6) NOT NULL,
  `date` date NOT NULL,
  `last_consult_date` date NOT NULL,
  `consultant_id` int(11) DEFAULT NULL,
  `referral_from_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_customer`
--

INSERT INTO `service_customer` (`id`, `phone`, `sns`, `name`, `status`, `gender`, `source`, `date`, `last_consult_date`, `consultant_id`, `referral_from_id`) VALUES
(1, '17088505529', '505529', '高拱', 2, 1, 1, '2018-10-23', '2018-10-23', 1, NULL),
(2, '15821312312', '505529', '徐阶', 2, 1, 1, '2018-10-23', '2018-10-23', 1, NULL),
(3, '18850932031', '505529', '张居正', 2, 1, 1, '2018-10-23', '2018-10-23', 1, NULL),
(4, '18865432100', '505529', '曾国藩', 2, 1, 1, '2018-10-23', '2018-10-23', NULL, NULL),
(5, '18865432109', '505529', '左宗棠', 2, 1, 2, '2018-10-23', '2018-10-23', NULL, 4),
(6, '17188505529', '505529', '李鸿章', 2, 1, 2, '2018-10-23', '2018-10-23', NULL, 4),
(7, '13821312312', '505529', '张之洞', 2, 1, 1, '2018-10-23', '2018-10-23', NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `service_customerinfo`
--

CREATE TABLE `service_customerinfo` (
  `id` int(11) NOT NULL,
  `education` int(11) DEFAULT NULL,
  `graduation_school` varchar(64) DEFAULT NULL,
  `major` varchar(64) DEFAULT NULL,
  `experience` int(11) DEFAULT NULL,
  `work_status` int(11) DEFAULT NULL,
  `company` varchar(64) DEFAULT NULL,
  `salary` varchar(64) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_customerinfo`
--

INSERT INTO `service_customerinfo` (`id`, `education`, `graduation_school`, `major`, `experience`, `work_status`, `company`, `salary`, `customer_id`) VALUES
(1, 1, '123', '123', 1, 1, '12321', '12312', 1),
(2, 2, '123', '123', 3, 1, '12321', '12312', 4);

-- --------------------------------------------------------

--
-- 表的结构 `service_customer_course`
--

CREATE TABLE `service_customer_course` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_customer_course`
--

INSERT INTO `service_customer_course` (`id`, `customer_id`, `course_id`) VALUES
(1, 1, 2),
(2, 2, 2),
(3, 2, 3),
(4, 3, 4),
(5, 3, 5),
(6, 4, 2),
(7, 4, 4),
(8, 5, 3),
(9, 5, 5),
(10, 6, 5),
(11, 7, 1);

-- --------------------------------------------------------

--
-- 表的结构 `service_paymentrecord`
--

CREATE TABLE `service_paymentrecord` (
  `id` int(11) NOT NULL,
  `pay_type` int(11) NOT NULL,
  `paid_fee` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `confirm_date` datetime(6) DEFAULT NULL,
  `note` longtext,
  `apply_date` datetime(6) NOT NULL,
  `classinfo_id` int(11) DEFAULT NULL,
  `confirm_user_id` int(11) DEFAULT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_paymentrecord`
--

INSERT INTO `service_paymentrecord` (`id`, `pay_type`, `paid_fee`, `status`, `confirm_date`, `note`, `apply_date`, `classinfo_id`, `confirm_user_id`, `consultant_id`, `customer_id`) VALUES
(1, 1, 1231, 1, '2018-01-01 00:00:00.000000', '', '2018-10-25 16:10:12.769302', 1, 1, 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `service_student`
--

CREATE TABLE `service_student` (
  `id` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `emergency_contract` varchar(32) DEFAULT NULL,
  `company` varchar(128) DEFAULT NULL,
  `position` varchar(64) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `welfare` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_student`
--

INSERT INTO `service_student` (`id`, `username`, `password`, `emergency_contract`, `company`, `position`, `salary`, `welfare`, `date`, `memo`, `customer_id`) VALUES
(1, 'gaogong', '', NULL, '明朝', '内阁阁老', 12312, NULL, NULL, NULL, 1),
(2, 'xuejie', '', NULL, '明朝', '内阁阁老', 12312, NULL, NULL, NULL, 2),
(3, 'zengguogan', '', NULL, '清朝', '两江总督', 123213, '23112', '2018-02-21', '21321321', 4);

-- --------------------------------------------------------

--
-- 表的结构 `service_student_classinfo`
--

CREATE TABLE `service_student_classinfo` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `classinfo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_student_classinfo`
--

INSERT INTO `service_student_classinfo` (`id`, `student_id`, `classinfo_id`) VALUES
(1, 1, 1),
(2, 1, 3),
(4, 2, 1),
(3, 2, 4),
(5, 3, 2);

-- --------------------------------------------------------

--
-- 表的结构 `service_studyrecord`
--

CREATE TABLE `service_studyrecord` (
  `id` int(11) NOT NULL,
  `record` varchar(64) NOT NULL,
  `score` int(11) NOT NULL,
  `homework_note` varchar(255) DEFAULT NULL,
  `homework` varchar(100) DEFAULT NULL,
  `stu_memo` longtext,
  `date` datetime(6) DEFAULT NULL,
  `course_record_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `service_studyrecord`
--

INSERT INTO `service_studyrecord` (`id`, `record`, `score`, `homework_note`, `homework`, `stu_memo`, `date`, `course_record_id`, `student_id`) VALUES
(1, 'checked', -1, NULL, '', NULL, NULL, 1, 1),
(2, 'checked', -1, NULL, '', NULL, NULL, 1, 2),
(3, 'checked', -1, NULL, '', NULL, NULL, 2, 3);

-- --------------------------------------------------------

--
-- 表的结构 `system_classinfo`
--

CREATE TABLE `system_classinfo` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `semester` smallint(6) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `openday` date DEFAULT NULL,
  `endday` date DEFAULT NULL,
  `note` longtext,
  `addtime` datetime(6) NOT NULL,
  `lasttime` datetime(6) NOT NULL,
  `admin_id` int(11) DEFAULT NULL,
  `college_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `tutor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_classinfo`
--

INSERT INTO `system_classinfo` (`id`, `title`, `semester`, `price`, `openday`, `endday`, `note`, `addtime`, `lasttime`, `admin_id`, `college_id`, `course_id`, `tutor_id`) VALUES
(1, 'Python全栈', 1, '12800.00', '2018-09-10', NULL, '', '2018-10-23 18:26:52.157665', '2018-10-24 14:24:57.032714', 1, 1, 1, 8),
(2, 'Linux架构师', 11, '15800.00', '2018-09-10', NULL, '', '2018-10-24 14:22:38.245678', '2018-10-24 14:31:36.594196', 1, 1, 2, 8),
(3, '大数据', 10, '18990.00', '2018-09-10', NULL, '', '2018-10-24 14:25:30.675852', '2018-10-24 14:25:30.675852', 1, 1, 3, 8),
(4, 'DBA', 1, '12800.00', '2018-09-10', NULL, '', '2018-10-24 14:30:13.081952', '2018-10-24 14:30:13.081952', 1, 2, 4, 7),
(5, '区块链', 5, '21800.00', '2018-09-10', NULL, '', '2018-10-24 14:31:26.340946', '2018-10-24 14:31:26.340946', 1, 3, 5, 7);

-- --------------------------------------------------------

--
-- 表的结构 `system_college`
--

CREATE TABLE `system_college` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `alias` varchar(12) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `address` varchar(64) NOT NULL,
  `openday` date DEFAULT NULL,
  `note` longtext,
  `addtime` datetime(6) NOT NULL,
  `lasttime` datetime(6) NOT NULL,
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_college`
--

INSERT INTO `system_college` (`id`, `title`, `alias`, `cover`, `phone`, `address`, `openday`, `note`, `addtime`, `lasttime`, `admin_id`) VALUES
(1, '北京校区', '北京', '', '17088505529', '北京沙河', '2018-09-10', '', '2018-10-23 18:23:16.779990', '2018-10-23 18:23:16.779990', 1),
(2, '上海校区', '上海', '', '15821312312', '上海浦东', '2018-09-10', '', '2018-10-23 18:23:33.867408', '2018-10-23 18:23:33.867408', 1),
(3, '深圳校区', '深圳', '', '18850932031', '深圳南山', '2018-09-10', '', '2018-10-23 18:23:46.802693', '2018-10-23 18:23:46.802693', 1);

-- --------------------------------------------------------

--
-- 表的结构 `system_course`
--

CREATE TABLE `system_course` (
  `id` int(11) NOT NULL,
  `title` varchar(32) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `lasttime` datetime(6) NOT NULL,
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_course`
--

INSERT INTO `system_course` (`id`, `title`, `addtime`, `lasttime`, `admin_id`) VALUES
(1, 'Python全栈', '2018-10-23 18:24:31.056375', '2018-10-23 18:24:31.056375', 1),
(2, 'Linux架构师', '2018-10-23 18:24:47.753222', '2018-10-23 18:24:47.753222', 1),
(3, '大数据开发', '2018-10-23 18:25:11.587286', '2018-10-23 18:25:11.587286', 1),
(4, 'MYSQL DBA', '2018-10-23 18:25:36.003108', '2018-10-23 18:25:36.003108', 1),
(5, 'GO语言和区块链', '2018-10-23 18:25:48.801994', '2018-10-23 18:25:48.801994', 1);

-- --------------------------------------------------------

--
-- 表的结构 `system_department`
--

CREATE TABLE `system_department` (
  `id` int(11) NOT NULL,
  `title` varchar(16) NOT NULL,
  `code` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_department`
--

INSERT INTO `system_department` (`id`, `title`, `code`) VALUES
(1, '市场', 'marketing'),
(2, '教学', 'training'),
(3, '财务', 'accounting'),
(4, '后勤', 'support');

-- --------------------------------------------------------

--
-- 表的结构 `system_userinfo`
--

CREATE TABLE `system_userinfo` (
  `id` int(11) NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `name` varchar(16) NOT NULL,
  `phone` varchar(32) NOT NULL,
  `gender` int(11) NOT NULL,
  `depart_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_userinfo`
--

INSERT INTO `system_userinfo` (`id`, `username`, `password`, `email`, `name`, `phone`, `gender`, `depart_id`) VALUES
(1, 'maali', NULL, NULL, '吗阿里', '17088505529', 1, 1),
(2, 'matengxu', NULL, NULL, '吗腾讯', '18850932031', 1, 2),
(3, 'libaidu', NULL, NULL, '里百度', '15821312312', 1, 3),
(4, 'liujingdong', NULL, NULL, '刘京东', '18850992031', 1, 1),
(5, 'renhuawei', NULL, NULL, '人华为', '18865432100', 1, 2),
(6, 'qiujinshan', NULL, NULL, '求金山', '18865432109', 1, 2),
(7, 'wangwanda', NULL, NULL, '王万达', '15821312312', 1, 2),
(8, 'guiguzi', NULL, NULL, '鬼谷子', '17088505529', 1, 2),
(9, 'leimi', NULL, NULL, '雷米', '15821312312', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `system_userinfo_roles`
--

CREATE TABLE `system_userinfo_roles` (
  `id` int(11) NOT NULL,
  `userinfo_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `system_userinfo_roles`
--

INSERT INTO `system_userinfo_roles` (`id`, `userinfo_id`, `role_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(4, 3, 1),
(5, 4, 4),
(6, 5, 1),
(7, 6, 2),
(10, 7, 5),
(9, 8, 5),
(11, 9, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `rbac_menu`
--
ALTER TABLE `rbac_menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rbac_permission`
--
ALTER TABLE `rbac_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `url` (`url`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `rbac_permission_menu_id_3dcc68be_fk_rbac_menu_id` (`menu_id`),
  ADD KEY `rbac_permission_parent_id_bcb411ef_fk_rbac_permission_id` (`parent_id`);

--
-- Indexes for table `rbac_role`
--
ALTER TABLE `rbac_role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rbac_role_permissions`
--
ALTER TABLE `rbac_role_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rbac_role_permissions_role_id_permission_id_d01303da_uniq` (`role_id`,`permission_id`),
  ADD KEY `rbac_role_permission_permission_id_f5e1e866_fk_rbac_perm` (`permission_id`);

--
-- Indexes for table `service_changerecord`
--
ALTER TABLE `service_changerecord`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`),
  ADD KEY `service_changerecord_admin_id_f8d9c549_fk_system_userinfo_id` (`admin_id`),
  ADD KEY `service_changerecord_origin_class_id_3a607537_fk_system_cl` (`origin_class_id`),
  ADD KEY `service_changerecord_target_class_id_0a27a31a_fk_system_cl` (`target_class_id`);

--
-- Indexes for table `service_consultrecord`
--
ALTER TABLE `service_consultrecord`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_consultrecor_consultant_id_d91cbc78_fk_system_us` (`consultant_id`),
  ADD KEY `service_consultrecor_customer_id_fe669d1b_fk_service_c` (`customer_id`);

--
-- Indexes for table `service_courserecord`
--
ALTER TABLE `service_courserecord`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_courserecord_teacher_id_7ee50b01_fk_system_userinfo_id` (`teacher_id`),
  ADD KEY `service_courserecord_classinfo_id_df066656_fk_system_cl` (`classinfo_id`);

--
-- Indexes for table `service_customer`
--
ALTER TABLE `service_customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `service_customer_consultant_id_8e4ba380_fk_system_userinfo_id` (`consultant_id`),
  ADD KEY `service_customer_referral_from_id_6d560faf_fk_service_c` (`referral_from_id`);

--
-- Indexes for table `service_customerinfo`
--
ALTER TABLE `service_customerinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`);

--
-- Indexes for table `service_customer_course`
--
ALTER TABLE `service_customer_course`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `service_customer_course_customer_id_course_id_39f9b0d3_uniq` (`customer_id`,`course_id`),
  ADD KEY `service_customer_course_course_id_a547e065_fk_system_course_id` (`course_id`);

--
-- Indexes for table `service_paymentrecord`
--
ALTER TABLE `service_paymentrecord`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_paymentrecor_classinfo_id_d211e2b3_fk_system_cl` (`classinfo_id`),
  ADD KEY `service_paymentrecor_confirm_user_id_66db17f0_fk_system_us` (`confirm_user_id`),
  ADD KEY `service_paymentrecor_consultant_id_a97b71e4_fk_system_us` (`consultant_id`),
  ADD KEY `service_paymentrecor_customer_id_c3577d38_fk_service_c` (`customer_id`);

--
-- Indexes for table `service_student`
--
ALTER TABLE `service_student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`);

--
-- Indexes for table `service_student_classinfo`
--
ALTER TABLE `service_student_classinfo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `service_student_classinfo_student_id_classinfo_id_18b349ae_uniq` (`student_id`,`classinfo_id`),
  ADD KEY `service_student_clas_classinfo_id_67e977d2_fk_system_cl` (`classinfo_id`);

--
-- Indexes for table `service_studyrecord`
--
ALTER TABLE `service_studyrecord`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_studyrecord_course_record_id_c392203b_fk_service_c` (`course_record_id`),
  ADD KEY `service_studyrecord_student_id_45ab8e22_fk_service_student_id` (`student_id`);

--
-- Indexes for table `system_classinfo`
--
ALTER TABLE `system_classinfo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `system_classinfo_admin_id_9e468222_fk_system_userinfo_id` (`admin_id`),
  ADD KEY `system_classinfo_college_id_fec7e5ca_fk_system_college_id` (`college_id`),
  ADD KEY `system_classinfo_course_id_bb2d27e7_fk_system_course_id` (`course_id`),
  ADD KEY `system_classinfo_tutor_id_1bffad87_fk_system_userinfo_id` (`tutor_id`);

--
-- Indexes for table `system_college`
--
ALTER TABLE `system_college`
  ADD PRIMARY KEY (`id`),
  ADD KEY `system_college_admin_id_daef6903_fk_system_userinfo_id` (`admin_id`);

--
-- Indexes for table `system_course`
--
ALTER TABLE `system_course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `system_course_admin_id_630da0c2_fk_system_userinfo_id` (`admin_id`);

--
-- Indexes for table `system_department`
--
ALTER TABLE `system_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `system_userinfo`
--
ALTER TABLE `system_userinfo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `system_userinfo_depart_id_834a2abc_fk_system_department_id` (`depart_id`);

--
-- Indexes for table `system_userinfo_roles`
--
ALTER TABLE `system_userinfo_roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `system_userinfo_roles_userinfo_id_role_id_0969c0d2_uniq` (`userinfo_id`,`role_id`),
  ADD KEY `system_userinfo_roles_role_id_d60605a3_fk_rbac_role_id` (`role_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;
--
-- 使用表AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- 使用表AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- 使用表AUTO_INCREMENT `rbac_menu`
--
ALTER TABLE `rbac_menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `rbac_permission`
--
ALTER TABLE `rbac_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `rbac_role`
--
ALTER TABLE `rbac_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `rbac_role_permissions`
--
ALTER TABLE `rbac_role_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `service_changerecord`
--
ALTER TABLE `service_changerecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `service_consultrecord`
--
ALTER TABLE `service_consultrecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `service_courserecord`
--
ALTER TABLE `service_courserecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `service_customer`
--
ALTER TABLE `service_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- 使用表AUTO_INCREMENT `service_customerinfo`
--
ALTER TABLE `service_customerinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `service_customer_course`
--
ALTER TABLE `service_customer_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- 使用表AUTO_INCREMENT `service_paymentrecord`
--
ALTER TABLE `service_paymentrecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- 使用表AUTO_INCREMENT `service_student`
--
ALTER TABLE `service_student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `service_student_classinfo`
--
ALTER TABLE `service_student_classinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `service_studyrecord`
--
ALTER TABLE `service_studyrecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `system_classinfo`
--
ALTER TABLE `system_classinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `system_college`
--
ALTER TABLE `system_college`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `system_course`
--
ALTER TABLE `system_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `system_department`
--
ALTER TABLE `system_department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- 使用表AUTO_INCREMENT `system_userinfo`
--
ALTER TABLE `system_userinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用表AUTO_INCREMENT `system_userinfo_roles`
--
ALTER TABLE `system_userinfo_roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `rbac_permission`
--
ALTER TABLE `rbac_permission`
  ADD CONSTRAINT `rbac_permission_menu_id_3dcc68be_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`),
  ADD CONSTRAINT `rbac_permission_parent_id_bcb411ef_fk_rbac_permission_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_permission` (`id`);

--
-- 限制表 `rbac_role_permissions`
--
ALTER TABLE `rbac_role_permissions`
  ADD CONSTRAINT `rbac_role_permission_permission_id_f5e1e866_fk_rbac_perm` FOREIGN KEY (`permission_id`) REFERENCES `rbac_permission` (`id`),
  ADD CONSTRAINT `rbac_role_permissions_role_id_d10416cb_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`);

--
-- 限制表 `service_changerecord`
--
ALTER TABLE `service_changerecord`
  ADD CONSTRAINT `service_changerecord_admin_id_f8d9c549_fk_system_userinfo_id` FOREIGN KEY (`admin_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `service_changerecord_origin_class_id_3a607537_fk_system_cl` FOREIGN KEY (`origin_class_id`) REFERENCES `system_classinfo` (`id`),
  ADD CONSTRAINT `service_changerecord_student_id_f098e9a2_fk_service_student_id` FOREIGN KEY (`student_id`) REFERENCES `service_student` (`id`),
  ADD CONSTRAINT `service_changerecord_target_class_id_0a27a31a_fk_system_cl` FOREIGN KEY (`target_class_id`) REFERENCES `system_classinfo` (`id`);

--
-- 限制表 `service_consultrecord`
--
ALTER TABLE `service_consultrecord`
  ADD CONSTRAINT `service_consultrecor_consultant_id_d91cbc78_fk_system_us` FOREIGN KEY (`consultant_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `service_consultrecor_customer_id_fe669d1b_fk_service_c` FOREIGN KEY (`customer_id`) REFERENCES `service_customer` (`id`);

--
-- 限制表 `service_courserecord`
--
ALTER TABLE `service_courserecord`
  ADD CONSTRAINT `service_courserecord_classinfo_id_df066656_fk_system_cl` FOREIGN KEY (`classinfo_id`) REFERENCES `system_classinfo` (`id`),
  ADD CONSTRAINT `service_courserecord_teacher_id_7ee50b01_fk_system_userinfo_id` FOREIGN KEY (`teacher_id`) REFERENCES `system_userinfo` (`id`);

--
-- 限制表 `service_customer`
--
ALTER TABLE `service_customer`
  ADD CONSTRAINT `service_customer_consultant_id_8e4ba380_fk_system_userinfo_id` FOREIGN KEY (`consultant_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `service_customer_referral_from_id_6d560faf_fk_service_c` FOREIGN KEY (`referral_from_id`) REFERENCES `service_customer` (`id`);

--
-- 限制表 `service_customerinfo`
--
ALTER TABLE `service_customerinfo`
  ADD CONSTRAINT `service_customerinfo_customer_id_e4740ee8_fk_service_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `service_customer` (`id`);

--
-- 限制表 `service_customer_course`
--
ALTER TABLE `service_customer_course`
  ADD CONSTRAINT `service_customer_cou_customer_id_4f93da4a_fk_service_c` FOREIGN KEY (`customer_id`) REFERENCES `service_customer` (`id`),
  ADD CONSTRAINT `service_customer_course_course_id_a547e065_fk_system_course_id` FOREIGN KEY (`course_id`) REFERENCES `system_course` (`id`);

--
-- 限制表 `service_paymentrecord`
--
ALTER TABLE `service_paymentrecord`
  ADD CONSTRAINT `service_paymentrecor_classinfo_id_d211e2b3_fk_system_cl` FOREIGN KEY (`classinfo_id`) REFERENCES `system_classinfo` (`id`),
  ADD CONSTRAINT `service_paymentrecor_confirm_user_id_66db17f0_fk_system_us` FOREIGN KEY (`confirm_user_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `service_paymentrecor_consultant_id_a97b71e4_fk_system_us` FOREIGN KEY (`consultant_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `service_paymentrecor_customer_id_c3577d38_fk_service_c` FOREIGN KEY (`customer_id`) REFERENCES `service_customer` (`id`);

--
-- 限制表 `service_student`
--
ALTER TABLE `service_student`
  ADD CONSTRAINT `service_student_customer_id_dfed4d49_fk_service_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `service_customer` (`id`);

--
-- 限制表 `service_student_classinfo`
--
ALTER TABLE `service_student_classinfo`
  ADD CONSTRAINT `service_student_clas_classinfo_id_67e977d2_fk_system_cl` FOREIGN KEY (`classinfo_id`) REFERENCES `system_classinfo` (`id`),
  ADD CONSTRAINT `service_student_clas_student_id_085d1150_fk_service_s` FOREIGN KEY (`student_id`) REFERENCES `service_student` (`id`);

--
-- 限制表 `service_studyrecord`
--
ALTER TABLE `service_studyrecord`
  ADD CONSTRAINT `service_studyrecord_course_record_id_c392203b_fk_service_c` FOREIGN KEY (`course_record_id`) REFERENCES `service_courserecord` (`id`),
  ADD CONSTRAINT `service_studyrecord_student_id_45ab8e22_fk_service_student_id` FOREIGN KEY (`student_id`) REFERENCES `service_student` (`id`);

--
-- 限制表 `system_classinfo`
--
ALTER TABLE `system_classinfo`
  ADD CONSTRAINT `system_classinfo_admin_id_9e468222_fk_system_userinfo_id` FOREIGN KEY (`admin_id`) REFERENCES `system_userinfo` (`id`),
  ADD CONSTRAINT `system_classinfo_college_id_fec7e5ca_fk_system_college_id` FOREIGN KEY (`college_id`) REFERENCES `system_college` (`id`),
  ADD CONSTRAINT `system_classinfo_course_id_bb2d27e7_fk_system_course_id` FOREIGN KEY (`course_id`) REFERENCES `system_course` (`id`),
  ADD CONSTRAINT `system_classinfo_tutor_id_1bffad87_fk_system_userinfo_id` FOREIGN KEY (`tutor_id`) REFERENCES `system_userinfo` (`id`);

--
-- 限制表 `system_college`
--
ALTER TABLE `system_college`
  ADD CONSTRAINT `system_college_admin_id_daef6903_fk_system_userinfo_id` FOREIGN KEY (`admin_id`) REFERENCES `system_userinfo` (`id`);

--
-- 限制表 `system_course`
--
ALTER TABLE `system_course`
  ADD CONSTRAINT `system_course_admin_id_630da0c2_fk_system_userinfo_id` FOREIGN KEY (`admin_id`) REFERENCES `system_userinfo` (`id`);

--
-- 限制表 `system_userinfo`
--
ALTER TABLE `system_userinfo`
  ADD CONSTRAINT `system_userinfo_depart_id_834a2abc_fk_system_department_id` FOREIGN KEY (`depart_id`) REFERENCES `system_department` (`id`);

--
-- 限制表 `system_userinfo_roles`
--
ALTER TABLE `system_userinfo_roles`
  ADD CONSTRAINT `system_userinfo_roles_role_id_d60605a3_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`),
  ADD CONSTRAINT `system_userinfo_roles_userinfo_id_03ae0c21_fk_system_userinfo_id` FOREIGN KEY (`userinfo_id`) REFERENCES `system_userinfo` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
