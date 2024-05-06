"use client"

import { LessonModal } from "../../ui/dashboard/modals/lessonsModal";
import { ModalWrapper } from "@/app/ui/modalWrapper";
import { Lessons } from "@/app/ui/dashboard/lessons";
import { Suspense } from "react";
import { LessonsSkeleton } from "@/app/ui/skeletons";

export default function Page() {
  return (
    <Suspense fallback={<LessonsSkeleton />}>
      <ModalWrapper Component={Lessons} Modal={LessonModal} />
    </Suspense>
  );
}
