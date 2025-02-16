--
-- PostgreSQL database dump
--

-- Dumped from database version 12.17 (Ubuntu 12.17-1.pgdg22.04+1)
-- Dumped by pg_dump version 12.17 (Ubuntu 12.17-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(30) NOT NULL,
    is_spherical boolean,
    beauty_rating integer,
    radius_in_lightyears integer,
    height_in_lightyears integer
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: inhabitant; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.inhabitant (
    name character varying(30) NOT NULL,
    planet_id integer,
    inhabitant_id integer NOT NULL
);


ALTER TABLE public.inhabitant OWNER TO freecodecamp;

--
-- Name: inhabitants_inhabitant_id_new_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.inhabitants_inhabitant_id_new_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inhabitants_inhabitant_id_new_seq OWNER TO freecodecamp;

--
-- Name: inhabitants_inhabitant_id_new_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.inhabitants_inhabitant_id_new_seq OWNED BY public.inhabitant.inhabitant_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(30) NOT NULL,
    average_distance_from_planet_in_km integer,
    planet_id integer,
    type character varying(10)
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(30) NOT NULL,
    has_life boolean,
    short_description text,
    average_distance_from_star_in_au numeric(4,1),
    star_id integer,
    class character varying(1)
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(30) NOT NULL,
    age_in_millions_of_years integer,
    galaxy_id integer,
    class integer
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: inhabitant inhabitant_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.inhabitant ALTER COLUMN inhabitant_id SET DEFAULT nextval('public.inhabitants_inhabitant_id_new_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'Milky Way', true, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (2, 'Andromeda', true, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (3, 'Messier 87', false, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (4, 'Triangulum', true, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (5, 'Sobrero Galaxy', true, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (6, 'Whirlpool Galaxy', false, NULL, NULL, NULL);


--
-- Data for Name: inhabitant; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.inhabitant VALUES ('Mensch', 1, 1);
INSERT INTO public.inhabitant VALUES ('Hund', 1, 2);
INSERT INTO public.inhabitant VALUES ('Katze', 1, 3);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon', NULL, 1, NULL);
INSERT INTO public.moon VALUES (2, 'Io', NULL, 3, NULL);
INSERT INTO public.moon VALUES (3, 'Europa', NULL, 3, NULL);
INSERT INTO public.moon VALUES (4, 'Titan', NULL, 2, NULL);
INSERT INTO public.moon VALUES (5, 'Phobus', NULL, 8, NULL);
INSERT INTO public.moon VALUES (6, 'Deimos', NULL, 8, NULL);
INSERT INTO public.moon VALUES (7, 'Ganymede', NULL, 3, NULL);
INSERT INTO public.moon VALUES (8, 'Callisto', NULL, 3, NULL);
INSERT INTO public.moon VALUES (9, 'Amalthea', NULL, 3, NULL);
INSERT INTO public.moon VALUES (10, 'Rhea', NULL, 2, NULL);
INSERT INTO public.moon VALUES (11, 'Iapetus', NULL, 2, NULL);
INSERT INTO public.moon VALUES (12, 'Dione', NULL, 2, NULL);
INSERT INTO public.moon VALUES (13, 'Tethys', NULL, 2, NULL);
INSERT INTO public.moon VALUES (14, 'Enceladus', NULL, 2, NULL);
INSERT INTO public.moon VALUES (15, 'Mimas', NULL, 2, NULL);
INSERT INTO public.moon VALUES (16, 'Titania', NULL, 9, NULL);
INSERT INTO public.moon VALUES (17, 'Oberon', NULL, 9, NULL);
INSERT INTO public.moon VALUES (18, 'Ariel', NULL, 9, NULL);
INSERT INTO public.moon VALUES (19, 'Umbriel', NULL, 9, NULL);
INSERT INTO public.moon VALUES (20, 'Triton', NULL, 10, NULL);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Erde', true, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (2, 'Saturn', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (3, 'Jupiter', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (4, 'Trappist-1 A', false, NULL, NULL, 2, NULL);
INSERT INTO public.planet VALUES (5, 'Trappist-1 B', false, NULL, NULL, 2, NULL);
INSERT INTO public.planet VALUES (6, 'Mercury', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (7, 'Venus', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (8, 'Mars', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (9, 'Uranus', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (10, 'Neptune', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (11, 'Pluto', false, NULL, NULL, 1, NULL);
INSERT INTO public.planet VALUES (12, 'Trappist-1 C', false, NULL, NULL, 2, NULL);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'Solar System', 123, 1, NULL);
INSERT INTO public.star VALUES (2, 'Trappist-1', 124, 1, NULL);
INSERT INTO public.star VALUES (3, 'Keppler-186', 324, 1, NULL);
INSERT INTO public.star VALUES (4, 'M31 V1', 123, 2, NULL);
INSERT INTO public.star VALUES (5, 'S Andromedae', 124, 2, NULL);
INSERT INTO public.star VALUES (6, 'SN 1919A', NULL, 3, NULL);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 6, true);


--
-- Name: inhabitants_inhabitant_id_new_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.inhabitants_inhabitant_id_new_seq', 3, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 6, true);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: inhabitant inhabitants_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.inhabitant
    ADD CONSTRAINT inhabitants_name_key UNIQUE (name);


--
-- Name: inhabitant inhabitants_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.inhabitant
    ADD CONSTRAINT inhabitants_pkey PRIMARY KEY (inhabitant_id);


--
-- Name: moon moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_name_key UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: inhabitant inhabitants_planet; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.inhabitant
    ADD CONSTRAINT inhabitants_planet FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: moon moons_planet; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moons_planet FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planets_star; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planets_star FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star stars_galaxy; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT stars_galaxy FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

