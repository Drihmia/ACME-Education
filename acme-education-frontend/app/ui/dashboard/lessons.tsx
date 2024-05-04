import Link from "next/link";
import { LessonCard } from "./lessonsCard";
import { Icon } from "@iconify/react/dist/iconify.js";
import { useAuth } from "@/app/context/authContext";
import useSWR from "swr";
import { LessonsSkeleton } from "../skeletons";
import { fetcher } from "@/app/lib/fetch";
import { lessonFormProps } from "@/app/types";

export const Lessons = ({
  openModal,
}: {
  openModal: (val: string) => void;
}) => {
  const { user } = useAuth()!;

  const { data: lessonsData, error } = useSWR(
    `http://127.0.0.1:5000/api/v1/teachers/${user?.user_id}/lessons`,
    fetcher,
    { suspense: true }
  );

  if (!lessonsData) return <LessonsSkeleton />;

  if (error) return <p>Error while fetching data...</p>;

  return (
    <div className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>My Lessons</h1>
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
        {lessonsData.length > 0 ? (
          <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
            <li className="w-full grid grid-cols-[1fr_7fr_1fr] p-2 bg-blue-50 rounded-md">
              <span className="font-semibold">S/N</span>
              <span className="font-semibold">Title</span>
              <span className="font-semibold">Public</span>
            </li>
            {lessonsData.map((lesson: lessonFormProps, i: number) => (
              <LessonCard key={`${i}`} index={i} lesson={lesson} openModal={openModal} />
            ))}
          </ul>
        ) : (
          <p>You do not have any published lessons.</p>
        )}
      </div>
    </div>
  );
};
