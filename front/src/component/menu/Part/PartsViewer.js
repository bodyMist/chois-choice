import axios from "axios";
import { useEffect, useState } from "react";
import PartsSelector from "./PartsSelector";
import ItemList from "./ItemList";
import Paging from "../../Paging";
//state 관리가 이상하게 꼬인듯...
export default function PartsViewer() {
    const [list, setList] = useState([]);
    const [fList, setFList] = useState([]);
    const [page, setPage] = useState(1);
    const getItemsByOption = (checkedItems) => {
        if (checkedItems.size != 0) {
            let array = [];
            [...checkedItems].map((items) => {
                const newList = fList.filter((listItem) => {
                    return JSON.stringify(listItem).search(items) != -1;
                });
                array = [...array, ...newList];
            });
            setList([...array]);
        } else {
            setList([...fList]);
        }
    };
    const setListByPage = (li) => {
        let array = [];
        let start = (page - 1) * 20;
        for (let i = start; i < start + 20; i++) {
            array = [...array, li[i]];
        }
        setList([...array]);
    };
    const pageHandler = (pg) => {
        console.log(pg);
        console.log(fList);
        console.log(list);
        setPage(pg);
        console.log(page);
        setListByPage(fList);
    };
    useEffect(() => {
        axios
            .get(`/component/cpu/list`)
            .then((response) => {
                setFList(response.data);
                setListByPage(response.data)
            })
            .catch((e) => {
                console.error(e);
            });
    }, []);
    useEffect(()=>{
        setList([...fList]);
        console.log(list);
    }, [fList])
    useEffect(()=>{
        console.log(page);
    },[page])
    const getPartItems = (id) => {
        //중분류 선택한것으로 백에서 정보 받아와야함.
        axios
            .get(`/component/${id}/list`)
            .then((response) => {
                setFList(response.data);
                setList(response.data);
            })
            .catch((e) => {
                console.error(e);
            });
    };
   
    return (
        <div className="prodlist_wrap">
            <PartsSelector
                getPartItems={getPartItems}
                getItemsByOption={getItemsByOption}
            />
            <ItemList list={list} />
            <Paging page={page} count={450} pageHandler={pageHandler} />
        </div>
    );
}
