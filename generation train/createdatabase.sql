CREATE TABLE IF NOT EXISTS `train_station`
(
    `id_Station` INT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `city` VARCHAR(50) NOT NULL,
    `id_language` INT NOT NULL,
    `nbt_train_track` INT NOT NULL,
    `have_terminals` boolean NOT NULL,
    `hourly` VARCHAR(50) NOT NULL,
    `id_company` INT NOT NULL,
    `passengers_per_year` INT NOT NULL,
    foreign key (id_company) references Company(id_company)
    foreign key (id_language) references Language(id_language)
);

CREATE TABLE IF NOT EXISTS `company`
(
    `id_company` INT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `phone` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `train`
(
    `id_train` INT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `journey`
(
    `id_journey` INT PRIMARY KEY,
    `id_station_1` INT NOT NULL,
    `id_station_2` INT NOT NULL,
    `distance` INT NOT NULL,
    foreign key (id_station_1) references Train_station(id_station),
    foreign key (id_station_2) references Train_station(id_station)
);

CREATE TABLE IF NOT EXISTS `train_journey`
(
    `id_train` INT NOT NULL,
    `id_journey` INT NOT NULL,
    foreign key (id_train) references Train(id_train),
    foreign key (id_journey) references Journey(id_journey)
);

CREATE TABLE IF NOT EXISTS `language`
(
    `id_language` INT NOT NULL,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `train_station_language`
(
    `id_station` INT NOT NULL,
    `id_language` INT NOT NULL,
    foreign key (id_station) references Train_station(id_Station),
    foreign key (id_language) references Language(id_language)
);

CREATE TABLE IF NOT EXISTS `service`
(
    `id_service` INT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS `train_station_service`
(
    `id_station` INT NOT NULL,
    `id_service` INT NOT NULL,
    foreign key (id_station) references Train_station(id_Station),
    foreign key (id_service) references Service(id_service)
);