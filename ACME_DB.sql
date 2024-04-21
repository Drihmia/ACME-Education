DROP DATABASE IF EXISTS acme;
create database if not exists ACME;
USE ACME;

-- ************************************** `institutions`

CREATE TABLE `institutions`
(
 `id`         varchar(64) NOT NULL ,
 `name`       varchar(128) NOT NULL ,
 `state`      varchar(64) NULL ,
 `city`       varchar(64) NULL ,
 `created_at` datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,
 `updated_at` datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`id`)
);


-- ************************************** `subjects`

CREATE TABLE `subjects`
(
 `id`          varchar(45) NOT NULL ,
 `name`        varchar(64) NOT NULL ,
 `lessons_ids` varchar(64) NOT NULL ,
 `teacher_ids` varchar(64) NOT NULL ,

PRIMARY KEY (`id`)
);



-- ************************************** `teachers`

CREATE TABLE `teachers`
(
 `id`             varchar(64) NOT NULL ,
 `fullname`       varchar(64) NOT NULL ,
 `institution_id` varchar(64) NOT NULL ,
 `subject_id`     varchar(45) NOT NULL ,
 `created_at`     datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,
 `updated_at`     datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`id`),
KEY `FK_1` (`institution_id`),
CONSTRAINT `FK_institution_id_teachers` FOREIGN KEY (`institution_id`) REFERENCES `institutions` (`id`),
CONSTRAINT `FK_subject_id_teachers` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`)
);

-- ************************************** `lesson`
CREATE TABLE `lessons`
(
 `id`             varchar(64) NOT NULL ,
 `name`           varchar(100) NOT NULL ,
 `download_link`  varchar(1024) NOT NULL ,
 `teacher_id`     varchar(64) NOT NULL ,
 `institution_id` varchar(64) NOT NULL , -- Removed the comma after varchar(64)
 `subject_id`     varchar(45) NOT NULL ,
 `created_at`     datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,
 `updated_at`     datetime NOT NULL  DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`id`),
KEY `FK_1` (`teacher_id`),
KEY `FK_2` (`institution_id`),
KEY `FK_3` (`subject_id`),
CONSTRAINT `FK_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`),
CONSTRAINT `FK_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institutions` (`id`),
CONSTRAINT `FK_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`)
);
