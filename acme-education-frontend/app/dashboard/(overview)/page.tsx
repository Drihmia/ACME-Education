"use client";

import { useAuth } from "@/app/context/authContext";
import { ProfileSkeleton } from "@/app/ui/skeletons";
import { Suspense } from "react";
import { useRouter } from "next/navigation";
// import { UpdateProfileModal } from "@/app/ui/dashboard/modals/updateProfileModal";
import { ProfileModalWrapper } from "@/app/ui/modalWrapper";
import { TeacherProfile } from "@/app/ui/dashboard/teacherProfile";
import { StudentProfile } from "@/app/ui/dashboard/studentProfile";
import { UpdateTeacherModal } from "@/app/ui/dashboard/modals/updateTeacherModal";
import { UpdateStudentModal } from "@/app/ui/dashboard/modals/updateStudentModal";

export default function Page() {
  const { user } = useAuth()!;
  const router = useRouter()

  if (!user) return router.push("/login")

  if (user.class === "Teacher") return <ProfileModalWrapper ProfileComponent={TeacherProfile} Modal={UpdateTeacherModal} user={user} />

  return <ProfileModalWrapper ProfileComponent={StudentProfile} Modal={UpdateStudentModal} user={user} />
}
