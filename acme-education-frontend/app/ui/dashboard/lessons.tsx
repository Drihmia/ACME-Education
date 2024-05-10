"use client";

import { useAuth } from "@/app/context/authContext";
import { LoadingSkeleton } from "../skeletons";
import { TeacherLessonsView } from "../teacherLessonsView";
import { StudentLessonsView } from "../studentLessonsView";

export const Lessons = ({
  openModal,
}: {
  openModal: (val: string) => void;
}) => {
  const { user } = useAuth()!;

  if (!user) return <LoadingSkeleton />;

  return (
    <div className="w-full grid gap-2">
      <h1 className={`text-2xl md:text-3xl font-bold`}>My Lessons</h1>
      {user.class === "Teacher" ? (
        <TeacherLessonsView
          openModal={openModal}
          user={user}
        />
      ) : (
        <StudentLessonsView
          openModal={openModal}
          user={user}
        />
      )}
    </div>
  );
};
