"use client";

import { lessonFormProps } from "@/app/types";
import { LessonCard } from "./dashboard/lessonsCard";

export const StudentLessonsView = ({
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
          List of available lessons
        </h2>
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
        <p>You do not have any lessons available.</p>
      )}
    </div>
  );
};
