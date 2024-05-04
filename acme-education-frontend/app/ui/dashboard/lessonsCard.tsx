import { deleteLesson } from "@/app/lib/fetch";
import { lessonFormProps } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import Link from "next/link";

interface lessonCardProps {
  index: number;
  lesson: lessonFormProps;
  openModal: (id: any) => void;
}

export const LessonCard = ({ index, lesson, openModal }: lessonCardProps) => {
  return (
    <li
      className={`group relative w-full grid grid-cols-[1fr_7fr_1fr] p-2 ${
        index % 2 == 0 ? "bg-blue-100" : "bg-blue-50"
      } hover:bg-blue-700 rounded-md hover:text-white cursor-pointer`}
      onClick={() => openModal(lesson)}
    >
      <span className="group-hover:opacity-0">{index + 1}.</span>
      <span>{lesson.name}</span>
      <span>{lesson.public == true ? "Yes" : "No"}</span>
      <div
        onClick={(e) => e.stopPropagation()}
        className="hidden absolute top-0 left-2 h-full group-hover:flex items-center"
      >
        <Link
          href={`/dashboard/lessons/edit/${lesson.id}`}
          className="w-8 h-8 flex items-center justify-center p-2 text-white hover:bg-white hover:text-black rounded"
        >
          <Icon icon="akar-icons:edit" />
        </Link>
        <button onClick={async() => {
            "use server"
            await deleteLesson(lesson.id!)
          }} className="w-8 h-8 flex items-center justify-center p-2 text-white hover:bg-white hover:text-black rounded">
          <Icon icon="material-symbols:delete-outline" />
        </button>
      </div>
    </li>
  );
};
