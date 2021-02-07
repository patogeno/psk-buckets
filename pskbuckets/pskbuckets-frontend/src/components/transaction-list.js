import { useState, useEffect } from "react"
import axios from "axios"
import styled from "styled-components"
import { transactions as data } from "./data"
import { SERVER_URL } from "../constants"
import moment from "moment"

const List = styled.table`
    text-align: center;
    border: 5px solid grey;
    border-spacing: 0;
    th {
        background-color: blue;
        color: white;
        font-weight: bold;
        padding: 0.5rem 0;
    }
    td {
        border-top: 1px solid blue;
        border-right: 1px solid blue;
        padding: 0.5rem 0;

        &:last-child {
            border-right: 0;
        }
    }
    width: 100%;
`

export default function TransactionList() {
    const [transactions, setTransactions] = useState([])

    useEffect(() => {
        const getTransactions = async () => {
            const options = {
                url: SERVER_URL + "api/transactions",
                method: "GET",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json;charset=UTF-8",
                },
            }
            try {
                const result = await axios(options)
                const ts = result.data.map((t) => {
                    return {
                        ...t,
                        datetime: moment.utc(t.datetime).format("DD/MM/YYYY"),
                    }
                })
                setTransactions(ts)
            } catch (error) {
                console.log("getTransactions", { options, error })
            }
        }
        getTransactions()
    }, [])

    return (
        <List>
            <tr>
                <th>Date</th>
                <th>Name</th>
                <th>Amount</th>
                <th>Bucket</th>
                <th>Category</th>
                <th>Is Real?</th>
            </tr>
            {transactions.map((transaction) => {
                return (
                    <tr key={transaction.id}>
                        <td>{transaction.datetime}</td>
                        <td>{transaction.name}</td>
                        <td>{transaction.amount}</td>
                        <td>{transaction.bucket_name}</td>
                        <td>{transaction.category_name}</td>
                        <td>{transaction.is_real ? "Real" : "Estimated"}</td>
                    </tr>
                )
            })}
        </List>
    )
}
