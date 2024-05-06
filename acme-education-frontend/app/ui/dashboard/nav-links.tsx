"use client";

import { Icon } from "@iconify/react/dist/iconify.js";
import clsx from "clsx";
import Link from "next/link";
import { usePathname } from "next/navigation";

// Map of links to display in the side navigation.
// Depending on the size of the application, this would be stored in a database.
const links = [
  { name: "Profile", href: "/dashboard", icon: <Icon icon="iconamoon:profile-circle-fill" /> },
  // {
  //   name: "Institutions",
  //   href: "/dashboard/institutions",
  //   icon: <Icon icon="gridicons:institution" />,
  // },
  // {
  //   name: "Subjects",
  //   href: "/dashboard/subjects",
  //   icon: <Icon icon="mdi:text-subject" />,
  // },
  {
    name: "Lessons",
    href: "/dashboard/lessons",
    icon: <Icon icon="material-symbols-light:library-books-outline" />,
  },
];

export const NavLinks = () => {
  const pathname = usePathname();
  return (
    <>
      {links.map((link) => {
        return (
          <Link
            key={link.name}
            href={link.href}
            className={clsx(
              `flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3`,
              {
                "bg-sky-100 text-blue-600": pathname === link.href,
              }
            )}
          >
            {link.icon}
            <p className="hidden md:block">{link.name}</p>
          </Link>
        );
      })}
    </>
  );
}
