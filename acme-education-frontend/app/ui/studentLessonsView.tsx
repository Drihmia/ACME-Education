"use client";

import { lessonFormProps, subjectProps } from "@/app/types";
import { LessonCard } from "./dashboard/lessonsCard";
import { FilterForm } from "./filterForm";
import { useState } from "react";

export const StudentLessonsView = ({
  user_class,
  lessons,
  subjects,
  openModal,
}: {
  user_class: string;
  lessons: lessonFormProps[];
  subjects: subjectProps[];
  openModal: (val: string) => void;
}) => {
  console.log(lessons);
  
  const [filteredLessons, setFilteredLessons] =
  useState<lessonFormProps[]>(lessons);

  return (
    <div className="w-full flex flex-col gap-2">
      <div className="w-full flex items-center justify-between py-4">
        <h2 className="text-xl md:text-2xl font-semibold">
          List of available lessons
        </h2>
      </div>
      <FilterForm subjects={subjects} lessons={lessons} setLessons={setFilteredLessons} />
      {filteredLessons.length > 0 ? (
        <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
          <li className="w-full grid grid-cols-[1fr_7fr_1fr] p-2 bg-blue-50 rounded-md">
            <span className="font-semibold">S/N</span>
            <span className="font-semibold">Title</span>
            <span className="font-semibold">Public</span>
          </li>
          {filteredLessons.map((lesson: lessonFormProps, i: number) => (
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
        <p>You do not have any lessons available.</p>
      )}
    </div>
  );
};
