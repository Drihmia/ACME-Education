import React from "react";
import { fetcher } from "../../lib/fetch";
import { User } from "../../types";
import { Icon } from "@iconify/react/dist/iconify.js";
import useSWR, { mutate } from "swr";
import { ProfileSkeleton } from "../skeletons";

export const TeacherProfile = ({
  user,
  openModal,
}: {
  user: User;
  openModal: (item: any) => void;
}) => {
  const { data: profile, error } = useSWR(
    `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/${user.class.toLowerCase()}s/${user.user_id}`,
    fetcher
  );

  const { data: subjects } = useSWR(
    `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${user.user_id}/subjects`,
    fetcher
  );
  const { data: classes } = useSWR(
    `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${user.user_id}/classes`,
    fetcher
  );
  const { data: institutions } = useSWR(
    `https://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${user.user_id}/institutions`,
    fetcher
  );

  if (error) return <p>There was an error.</p>;

  if (!profile || !subjects || !institutions) return <ProfileSkeleton />;

  profile.subjects = subjects;
  profile.classes = classes;
  profile.institutions = institutions;

  return (
    <div className="w-full h-full flex flex-col gap-4 md:gap-8">
      <div className="w-full flex items-center justify-between">
        <h1 className={`text-2xl md:text-3xl font-bold`}>
          My Profile{" "}
          <span className="block text-lg font-semibold">{profile.last_name} {profile.first_name}</span>
        </h1>
        <button
          onClick={() => openModal(profile)}
          className="w-16 flex items-center gap-1 py-1 px-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize"
        >
          <Icon icon="mage:edit" /> Edit
        </button>
      </div>
      <div className="w-full h-full grid md:grid-cols-[1fr_4fr] gap-4 md:gap-8 py-4">
        <div className="w-full flex justify-center">
          <Icon fontSize={192} icon="lets-icons:user-box-light" />
        </div>
        <div className="w-full h-full flex flex-col justify-between p-4 md:p-8">
          <div className="w-full flex flex-col gap-2">
            <ul className="w-full flex flex-col gap-1">
              <li className="md:text-lg font-medium">
                Name:{" "}
                <span className="font-normal">
                  {profile.first_name} {profile.last_name}
                </span>
              </li>
              <li className="md:text-lg font-medium">
                Email: <span className="font-normal">{profile.email}</span>
              </li>
              <li className="md:text-lg font-medium">
                Gender:{" "}
                <span className="font-normal">
                  {profile.gender === "M" ? "Male" : "Female"}
                </span>
              </li>
              <li className="md:text-lg font-medium">
                City: <span className="font-normal">{profile.city}</span>
              </li>
            </ul>
          </div>
        </div>
        <div className="w-full col-span-full grid gap-4">
          <div className="text-lg md:text-xl font-medium">
            Institutions:
            {profile.institutions.length > 0 ? (
              <p className="w-full grid gap-2 md:grid-cols-2 lg:grid-cols-3 p-2 md:p-4">
                {profile.institutions.map((ins: any, i: number) => (
                  <span className="font-normal text-sm" key={`${i}`}>
                    {ins.name}
                  </span>
                ))}
              </p>
            ) : (
              <span className="font-normal text-sm block">
                You do not have any class.
              </span>
            )}
          </div>
          <div className="text-lg md:text-xl font-medium">
            Classes Taken:
            {profile.subjects.length > 0 ? (
              <p className="w-full grid gap-2 md:grid-cols-2 lg:grid-cols-3 p-2 md:p-4">
                {profile.classes.map((cls: any, i: number) => (
                  <span className="font-normal text-sm" key={`${i}`}>
                    {cls.name}
                  </span>
                ))}
              </p>
            ) : (
              <span className="font-normal text-sm block">
                You do not have any class.
              </span>
            )}
          </div>
          <div className="text-lg md:text-xl font-medium">
            Subjects Taught:
            {profile.subjects.length > 0 ? (
              <p className="w-full grid gap-2 md:grid-cols-2 lg:grid-cols-3 p-2 md:p-4">
                {profile.subjects.map((sub: any, i: number) => (
                  <span className="font-normal text-sm" key={`${i}`}>
                    {sub.name}
                  </span>
                ))}
              </p>
            ) : (
              <span className="font-normal text-sm block">
                You do not have any subject.
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
