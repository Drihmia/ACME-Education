"use client";

import { Icon } from "@iconify/react";
import Link from "next/link";
import { useState } from "react";
import { useAuth } from "@/app/context/authContext";

export const Header = () => {
  const { user } = useAuth()!
  const [navIsOpen, setNav] = useState(false);

  const handleNav = () => setNav((prev) => !prev);

  return (
    <header className="sticky top-0 left-0 w-full p-4 flex items-center justify-between shadow-lg bg-white z-20">
      <div className="flex items-center justify-between">
        <Link
          href={`/`}
          className="text-xl md:text-2xl md:py-2 uppercase font-bold"
        >
          ACME Education
        </Link>
        </div>
        {!user && (
          <div className="flex items-center font-bold">
            <p className="md:hidden uppercase">menu</p>
            <button
              onClick={handleNav}
              id="open_menu_btn"
              aria-label="open hamburger menu"
              className="p-2 sm:p-3 md:p-4 text-2xl md:hidden flex items-center justify-center hover:text-blue-700"
            >
              <Icon icon="ci:hamburger-md" />
            </button>
          </div>
        )}
      {!user && (
        <nav
          id="nav_overlay"
          className={`fixed md:static top-0 right-0 ${
            navIsOpen ? "translate-x-0" : "translate-x-full"
          } w-screen md:w-auto h-screen md:h-full md:translate-x-0 bg-black/25 z-20`}
        >
          <div
            id="nav"
            className={`fixed md:static top-0 right-0 ${
              navIsOpen ? "translate-x-0" : "translate-x-full"
            } w-full h-full md:translate-x-0 flex flex-col md:flex-row items-center gap-4 p-4 md:p-0 transition-all duration-300 ease-linear bg-white z-50`}
          >
            <button
              onClick={handleNav}
              id="close_menu_btn"
              aria-label="close hamburger menu"
              className="self-end md:hidden text-2xl hover:text-red-500"
            >
              <Icon icon="zondicons:close-outline" />
            </button>
            <p className="md:hidden w-full text-center text-2xl uppercase font-bold">
              ACME Education
            </p>
            <ul
              onClick={handleNav}
              className="w-full flex items-center flex-col md:flex-row gap-4 sm:gap-6 md:gap-8 uppercase text-lg"
            >
              <li className="md:w-24 text-center py-1 border-b-2 border-white hover:border-black transition-all ease-linear duration-200 cursor-pointer">
                <Link href={`/`}>home</Link>
              </li>
              <li className="md:w-24 text-center py-1 border-b-2 border-white hover:border-black transition-all ease-linear duration-200 cursor-pointer">
                <Link href={`/about_us`}>about us</Link>
              </li>
              <li className="py-2 px-4 rounded-2xl bg-blue-100 text-black hover:text-white hover:bg-blue-700 font-medium transition-all ease-linear duration-200 cursor-pointer">
                <Link href={`/login`}>login</Link>
              </li>
            </ul>
          </div>
        </nav>
      )}
    </header>
  );
};
