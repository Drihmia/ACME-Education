import { deleteLesson } from "@/app/lib/fetch";
import { lessonFormProps } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import Link from "next/link";
import { mutate } from "swr";

interface lessonCardProps {
  index: number;
  lesson: lessonFormProps;
  openModal: (id: any) => void;
  user_class: string
}

export const LessonCard = ({ index, lesson, openModal, user_class }: lessonCardProps) => {
  
  return (
    <li
      className={`group relative w-full grid grid-cols-[0.75fr_5fr_2fr_2fr_0.5fr] p-2 ${
        index % 2 == 0 ? "bg-blue-100" : "bg-blue-50"
      } hover:bg-blue-700 rounded-md hover:text-white cursor-pointer`}
      onClick={() => openModal(lesson)}
    >
      <span className="group-hover:opacity-0 text-center">{index + 1}.</span>
      <span className="truncate">{lesson.name}</span>
      <span className="truncate">{lesson.subject}</span>
      <span className="truncate">{lesson.teacher}</span>
      <span className="">{lesson.public == true ? "Yes" : "No"}</span>
      { user_class == "Teacher" && (
        <div
        onClick={(e) => e.stopPropagation()}
        className="hidden absolute top-0 left-2 h-full group-hover:flex items-center"
      >
        <Link
          href={`/dashboard/lessons/edit/${lesson.id}`}
          className="w-6 h-6 flex items-center justify-center p-1 text-white hover:bg-white hover:text-black rounded"
        >
          <Icon icon="akar-icons:edit" />
        </Link>
        <button onClick={async () => {
              if (confirm("Are you sure you delete this lesson?")) {
                const res = await deleteLesson(lesson.id!);
                if (res["error"]) {
                  alert("Something went wrong.");
                } else {
                  mutate(`http://${process.env.NEXT_API_ADDRESS}/api/v1/teachers/${lesson.teacher_id}/lessons`)
                  alert("Lesson deleted");
                }
              }
            }} className="w-6 h-6 flex items-center justify-center p-1 text-white hover:bg-white hover:text-black rounded">
          <Icon icon="material-symbols:delete-outline" />
        </button>
      </div>
      )}
    </li>
  );
};
