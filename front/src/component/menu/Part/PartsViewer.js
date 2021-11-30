import axios from "axios";
import { useEffect, useState } from "react";
import PartsSelector from "./PartsSelector";
import ItemList from "./ItemList";

export default function PartsViewer() {
  const [list, setList] = useState([]);
  const [fList, setFList] = useState([]);
  const a = 'data';
  useEffect(() => {
      axios
          .get(`/component/cpu/list`)
          .then((response) => {
              setList(response.data);
              setFList(response.data);
          })
          .catch((e) => {
              console.error(e);
          });
          
  }, []);
  console.log(list)
  const getPartItems = (id) => {
      //중분류 선택한것으로 백에서 정보 받아와야함.
      axios
          .get(`/component/${id}/list`)
          .then((response) => {
              setList(response.data);
          })
          .catch((e) => {
              console.error(e);
          });
  };

  // 옵션 선택된 것으로 정보 필터링하는거 만들어야함.
  const getItemsByOption = (checkedItems) => {
    [...checkedItems].map((items)=>{
        const id = items.id;
        const title = items.title;
        const newList = list.filter((list) => list.component_component.manufacture == "인텔 코어i7-12세대");
        console.log(newList)
        const array = [...fList, ...newList];
        console.log(array);
        setFList(array);
    })
    console.log(fList)
    const otherArray= [...list, ...fList];
    setList(otherArray);
    console.log(checkedItems)
  }
  return (
      <div className="prodlist_wrap">
          <PartsSelector
              getPartItems={getPartItems}
              getItemsByOption={getItemsByOption}
          />
          <ItemList list={list} />
      </div>
  );
}