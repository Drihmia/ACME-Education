import React from "react";
import { fetcher } from "../../lib/fetch";
import { User } from "../../types";
import { Icon } from "@iconify/react/dist/iconify.js";
import useSWR, { mutate } from "swr";
import { ProfileSkeleton } from "../skeletons";

export const TeacherProfile = ({ user, openModal }: { user: User, openModal: (item: any) => void }) => {
  const { data: profile, error } = useSWR(
    `http://127.0.0.1:5000/api/v1/${user.class.toLowerCase()}s/${user.user_id}`,
    fetcher
  );
  
  const { data: subjectsList } = useSWR(
    `http://127.0.0.1:5000/api/v1/teachers/${user.user_id}/subjects`,
    fetcher
  );

  mutate(`http://127.0.0.1:5000/api/v1/teachers/${user.user_id}/subjects`)
  
  
  if (error) return <p>There was an error.</p>

  if (!profile || !subjectsList) return <ProfileSkeleton />

  return (
    <div className="w-full h-full flex flex-col gap-4 md:gap-8">
      <h1 className={`text-2xl md:text-3xl font-bold`}>
        My Profile <span className="block text-lg">ID: {profile.id}</span>
      </h1>
      <div className="w-full h-full grid md:grid-cols-[1fr_3fr] gap-4 md:gap-8">
        <div className="w-full flex justify-center">
          <Icon fontSize={192} icon="lets-icons:user-box-light" />
        </div>
        <div className="w-full h-full flex flex-col justify-between p-4 md:p-8">
          <div className="w-full flex flex-col gap-2">
          <ul className="w-full flex flex-col gap-1">
            <li className="text-lg md:text-xl font-medium">
              Name:{" "}
              <span className="font-normal">{profile.first_name} {profile.last_name}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Email: <span className="font-normal">{profile.email}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Gender:{" "}
              <span className="font-normal">{profile.gender}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              City:{" "}
              <span className="font-normal">{profile.city}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Institution:{" "}
              <span className="font-normal">{profile.institution}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Subjects:{" "}
              <span className="font-normal">{subjectsList.length > 0 ? subjectsList.map((sub: any) => sub.name).join(", ") : "You dont have any subjects" }</span>
            </li>
          </ul>
          </div>
          <button onClick={() => openModal(profile)} className="w-16 self-end flex items-center gap-1 py-1 px-2 mt-4 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize">
            <Icon icon="mage:edit" /> Edit
          </button>
        </div>
      </div>
    </div>
  );
};

