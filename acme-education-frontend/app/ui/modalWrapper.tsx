// wraps a component and a modal

import React, { useState } from "react";
import { lessonFormProps } from "../types";

interface props {
  Component: React.ComponentType<{
    openModal: (val: string) => void;
  }>;
  Modal: React.ComponentType<{
    closeModal: () => void;
    item: lessonFormProps;
  }>;
}


export const ModalWrapper = ({ Component, Modal }: props) => {
  const [isModal, setModal] = useState(false);
  const [selectedItem, setItem] = useState<any>();
  const openModal = (item: any) => {
    setModal(true);
    setItem(item);
  };
  const closeModal = () => setModal(false);
  return (
    <>
      <Component openModal={openModal} />
      {isModal && <Modal closeModal={closeModal} item={selectedItem} />}
    </>
  );
};
