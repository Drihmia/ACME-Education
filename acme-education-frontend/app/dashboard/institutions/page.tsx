"use client"

import { InstitutionsCard } from "@/app/ui/dashboard/institutionsCard";
import { InstitutionModal } from "@/app/ui/dashboard/modals/institutionModal";
import { Icon } from "@iconify/react/dist/iconify.js";
import { useState } from "react";

export default function Page() {
    const [isModal, setModal] = useState(false)
    const [selectedInstitution, setInstitution] = useState("")
    const handleModal = (item: string) => {
        setModal(prev => !prev)
        setInstitution(item)
    }
    const closeModal = () => setModal(false)

  return (
    <div className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>My Institutions</h1>
      <div className="w-full flex flex-col gap-2">
        <div className="w-full flex items-center justify-between py-4">
        <h2 className="text-xl md:text-2xl font-semibold">
          List of associated institutions
        </h2>
        <button className="w-48 flex items-center gap-1 p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize"><Icon icon="mdi:add-bold" /> Add New Institution</button>
        </div>
        <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
          <li className="w-full grid grid-cols-[1fr_6fr_2fr_2fr] p-2 bg-blue-50 rounded-md">
            <span className="font-semibold">S/N</span>
            <span className="font-semibold">Name</span>
            <span className="font-semibold">City</span>
            <span className="font-semibold">State</span>
          </li>
          {Array.from({ length: 10 }).map((_, i) => <InstitutionsCard key={`${i}`} index={i} openModal={handleModal} />)}
        </ul>
      </div>
      {isModal && <InstitutionModal closeModal={closeModal} institutionID={selectedInstitution} />}
    </div>
  );
}
