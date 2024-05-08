"use client";

import Link from "next/link";
import { Icon } from "@iconify/react/dist/iconify.js";
import { lessonFormProps } from "@/app/types";
import { LessonCard } from "./dashboard/lessonsCard";

export const TeacherLessonsView = ({
  user_class,
  lessons,
  openModal,
}: {
  user_class: string;
  lessons: lessonFormProps[];
  openModal: (val: string) => void;
}) => {
  return (
    <div className="w-full flex flex-col gap-2">
      <div className="w-full flex items-center justify-between py-4">
        <h2 className="text-xl md:text-2xl font-semibold">
          List of published lessons
        </h2>
        <Link
          href={`/dashboard/lessons/add`}
          className="w-48 flex items-center gap-1 p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize"
        >
          <Icon icon="mdi:add-bold" /> Publish New Lesson
        </Link>
      </div>
      {lessons.length > 0 ? (
        <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
          <li className="w-full grid grid-cols-[1fr_7fr_1fr] p-2 bg-blue-50 rounded-md">
            <span className="font-semibold">S/N</span>
            <span className="font-semibold">Title</span>
            <span className="font-semibold">Public</span>
          </li>
          {lessons.map((lesson: lessonFormProps, i: number) => (
            <LessonCard
              key={`${i}`}
              index={i}
              lesson={lesson}
              openModal={openModal}
              user_class={user_class}
            />
          ))}
        </ul>
      ) : (
        <p>You do not have any published lessons.</p>
      )}
    </div>
  );
};
