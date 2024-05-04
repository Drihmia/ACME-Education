"use client"

import { LessonModal } from "../../ui/dashboard/modals/lessonsModal";
import { ModalWrapper } from "@/app/ui/modalWrapper";
import { Lessons } from "@/app/ui/dashboard/lessons";

export default function Page() {
  return (
    <ModalWrapper Component={Lessons} Modal={LessonModal} />
  );
}
