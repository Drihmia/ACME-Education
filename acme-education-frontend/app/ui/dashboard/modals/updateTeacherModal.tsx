import React from "react";
import { Icon } from "@iconify/react/dist/iconify.js";
import { TeacherForm } from "../../teacherForm"


export const UpdateTeacherModal = ({
    closeModal,
    item,
  }: {
    closeModal: () => void;
    item: any;
  }) => {
    return (
      <div className="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-black/25">
        <div className="relative w-full max-w-4xl h-[512px] overflow-y-scroll p-4 md:p-8 flex flex-col justify-between gap-8 rounded-md bg-white">
          <button
            className="absolute top-0 right-0 p-2 text-2xl hover:text-red-700"
            onClick={closeModal}
            >
              <Icon icon="material-symbols:close" />
            </button>
            <TeacherForm action="update" profile={item} close={closeModal} />
        </div>
      </div>
    );
  };
  