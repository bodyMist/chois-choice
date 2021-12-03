import axios from "axios";
import { useEffect, useState } from "react";
import PartsSelector from "./PartsSelector";
import ItemList from "./ItemList";
import Paging from "../../Paging";
//state 관리가 이상하게 꼬인듯...
export default function PartsViewer() {
    
    const [page, setPage] = useState(1);
    const [list, setList] = useState([]);
    const [fList, setFList] = useState([]);

    useEffect(() => {
        axios
            .get(`/component/cpu/list`)
            .then((response) => {
                setFList([...response.data]);
                console.log(response.data.length)
                setListByPage([...response.data])
            })
            .catch((e) => {
                console.error(e);
            });
    }, []);
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
    const pageHandler = (pg) => {
        setPage(pg);
        let array = [];
        let start = (pg - 1) * 10;
        for (let i = start; i < start + 10; i++) {
            if(fList[i])
                array = [...array, fList[i]];
        }
        setList([...array]);
    };
    const setListByPage = (li) => {
        console.log(page)
        console.log(fList)
        console.log(list)
        console.log(li)
        let array = [];
        let start = (page - 1) * 10;
        for (let i = start; i < start + 10; i++) {
            array = [...array, li[i]];
        }
        setList([...array]);
    };
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
            <Paging page={page} count={fList.length} pageHandler={pageHandler}/>
        </div>
    );
}
