"use client";

import Link from "next/link";
import { Icon } from "@iconify/react/dist/iconify.js";
import { User } from "@/app/types";
import { FilterForm } from "./filterForm";
import { LessonsSkeleton } from "./skeletons";
import useSWR from "swr";
import { fetcher } from "../lib/fetch";

export const TeacherLessonsView = ({
  user,
  openModal,
}: {
  user: User;
  openModal: (val: string) => void;
}) => {

  const { data: lessons } = useSWR(
    user
      ? `http://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/${user.class.toLowerCase()}s/${
          user.user_id
        }/lessons`
      : null,
    fetcher
  );

  const { data: subjects } = useSWR(
    user
      ? `http://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/${user.class.toLowerCase()}s/${
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
          List of published lessons
        </h2>
        <Link
          href={`/dashboard/lessons/add`}
          className="w-48 flex items-center gap-1 p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize"
        >
          <Icon icon="mdi:add-bold" /> Publish New Lesson
        </Link>
      </div>
      <FilterForm subjects={subjects} lessons={lessons} openModal={openModal} user_class={user.class} />
    </div>
  );
};
