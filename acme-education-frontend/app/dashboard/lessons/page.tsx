"use client"

import { Icon } from "@iconify/react/dist/iconify.js";
import { useState } from "react";
import { LessonsCard } from "../../ui/dashboard/lessonsCard";
import { LessonModal } from "../../ui/dashboard/modals/lessonsModal";
import Link from "next/link";

export default function Page() {
    const [isModal, setModal] = useState(false)
    const [selectedLesson, setLesson] = useState("")
    const handleModal = (item: string) => {
        setModal(prev => !prev)
        setLesson(item)
    }
    const closeModal = () => setModal(false)

  return (
    <div className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>My Lessons</h1>
      <div className="w-full flex flex-col gap-2">
        <div className="w-full flex items-center justify-between py-4">
        <h2 className="text-xl md:text-2xl font-semibold">
          List of published lessons
        </h2>
        <Link href={`/dashboard/lessons/add`} className="w-48 flex items-center gap-1 p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize"><Icon icon="mdi:add-bold" /> Publish New Lesson</Link>
        </div>
        <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
          <li className="w-full grid grid-cols-[1fr_7fr_1fr] p-2 bg-blue-50 rounded-md">
            <span className="font-semibold">S/N</span>
            <span className="font-semibold">Title</span>
            <span className="font-semibold">Public</span>
          </li>
          {Array.from({ length: 10 }).map((_, i) => <LessonsCard key={`${i}`} index={i} openModal={handleModal} />)}
        </ul>
      </div>
      {isModal && <LessonModal closeModal={closeModal} lessonID={selectedLesson} />}
    </div>
  );
}
