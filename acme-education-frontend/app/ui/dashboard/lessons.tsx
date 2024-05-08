"use client";

import { useAuth } from "@/app/context/authContext";
import useSWR from "swr";
import { LessonsSkeleton } from "../skeletons";
import { fetcher } from "@/app/lib/fetch";
import { TeacherLessonsView } from "../teacherLessonsView";
import { StudentLessonsView } from "../studentLessonsView";

export const Lessons = ({
  openModal,
}: {
  openModal: (val: string) => void;
}) => {
  const { user } = useAuth()!;

  const { data: lessons, error } = useSWR(
    `http://127.0.0.1:5000/api/v1/${user?.class.toLowerCase()}s/${
      user?.user_id
    }/lessons`,
    fetcher
  );

  if (error) return <p>Error while fetching data...</p>;

  if (!lessons || !user) return <LessonsSkeleton />;

  return (
    <div className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>My Lessons</h1>
      {user.class === "Teacher" ? (
        <TeacherLessonsView lessons={lessons} openModal={openModal} user_class={user.class} />
      ) : (
        <StudentLessonsView lessons={lessons} openModal={openModal} user_class={user.class} />
      )}
    </div>
  );
};
