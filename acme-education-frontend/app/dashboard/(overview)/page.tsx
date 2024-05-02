"use client";

import { Icon } from "@iconify/react/dist/iconify.js";

export default function Page() {
  //   const {
  //     numberOfCustomers,
  //     numberOfInvoices,
  //     totalPaidInvoices,
  //     totalPendingInvoices,
  //   } = await fetchCardData();
  return (
    <main className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>
        My Profile <span className="block text-lg">ID: xxxx xxxx xxxx</span>
      </h1>

      <div className="w-full max-w-60 flex flex-col gap-2">
        <h2 className="text-xl md:text-2xl font-semibold">Personal Info</h2>
        <ul className="w-full flex flex-col gap-1">
          <li>
            First Name: <span className="font-medium">John</span>
          </li>
          <li>
            Last Name: <span className="font-medium">Doe</span>
          </li>
          <li>
            Email: <span className="font-medium">johndoe@example.com</span>
          </li>
        </ul>
        <button className="w-16 self-end flex items-center gap-1 py-1 px-2 mt-4 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize">
          <Icon icon="mage:edit" /> Edit
        </button>
      </div>
      <div className="w-full max-w-60 flex flex-col gap-2 mt-8">
        <h2 className="text-xl md:text-2xl font-semibold">Academic Info</h2>
        <ul className="w-full flex flex-col gap-1">
          <li>Number of Subjects: 100</li>
          <li>Number of Lessons: 100</li>
          <li>Number of Classes: 100</li>
          <li>Number of Institutions: 100</li>
        </ul>
      </div>
    </main>
  );
}
