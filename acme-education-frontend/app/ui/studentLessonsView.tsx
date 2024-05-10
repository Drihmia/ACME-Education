"use client";

import { User } from "@/app/types";
import { FilterForm } from "./filterForm";
import { LessonsSkeleton } from "./skeletons";
import { fetcher } from "../lib/fetch";
import useSWR from "swr";

export const StudentLessonsView = ({
  user,
  openModal,
}: {
  user: User;
  openModal: (val: string) => void;
}) => {
  const { data: lessons } = useSWR(
    user
      ? `http://127.0.0.1:5000/api/v1/${user.class.toLowerCase()}s/${
          user.user_id
        }/lessons`
      : null,
    fetcher
  );

  const { data: subjects } = useSWR(
    user
      ? `http://127.0.0.1:5000/api/v1/${user.class.toLowerCase()}s/${
          user.user_id
        }/subjects`
      : null,
    fetcher
  );
  
  if (!lessons || !subjects || !user) return <LessonsSkeleton />;


  return (
    <div className="w-full flex flex-col gap-2">
      <div className="w-full flex items-center justify-between py-4">
        <h2 className="text-xl md:text-2xl font-semibold">
          List of available lessons
        </h2>
      </div>
      <FilterForm subjects={subjects} lessons={lessons} openModal={openModal} user_class={user.class} />
    </div>
  );
};
