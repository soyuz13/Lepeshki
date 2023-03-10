# from __future__ import annotations
import json

from typing import Any, List, Optional

from pydantic import BaseModel


class Space(BaseModel):
    id: Optional[str]
    name: Optional[str]


class Creator(BaseModel):
    id: Optional[str]
    email: Optional[str]
    surname: Optional[Any]
    name: Optional[Any]
    patronymic: Optional[Any]
    lang: Optional[str]


class File(BaseModel):
    name: Optional[str]


class RecognitionTask1(BaseModel):
    id: Optional[str]
    source: Optional[str]


class Space1(BaseModel):
    id: Optional[str]
    trial: Optional[bool]


class File1(BaseModel):
    name: Optional[str]


class Page(BaseModel):
    number: Optional[int]
    url: Optional[str]
    file: Optional[File1]
    rotationAngle: Optional[int]


class HeaderPosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class Position(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class NamePosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class AmountWithoutVatPosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class Item(BaseModel):
    id: Optional[str]
    headerPosition: Optional[HeaderPosition]
    position: Optional[Position]
    recognizedSerialNumber: Optional[int]
    serialNumber: Optional[int]
    serialNumberPosition: Optional[Any]
    recognizedGoodCode: Optional[Any]
    goodCode: Optional[Any]
    goodCodePosition: Optional[Any]
    recognizedName: Optional[str]
    name: Optional[str]
    namePosition: Optional[NamePosition]
    recognizedGoodTypeCode: Optional[Any]
    goodTypeCodePosition: Optional[Any]
    recognizedUnitCode: Optional[Any]
    unitCodePosition: Optional[Any]
    recognizedUnit: Optional[str]
    unitName: Optional[str]
    unitPosition: Optional[Any]
    recognizedQuantity: Optional[int]
    quantity: Optional[int]
    quantityPosition: Optional[Any]
    recognizedPrice: Optional[float]
    price: Optional[float]
    pricePosition: Optional[Any]
    recognizedAmountWithoutVat: Optional[float]
    amountWithoutVat: Optional[float]
    amountWithoutVatPosition: Optional[AmountWithoutVatPosition]
    recognizedExcise: Optional[float]
    excise: Optional[float]
    excisePosition: Optional[Any]
    recognizedVatRate: Optional[str]
    vatRate: Optional[str]
    vatRatePosition: Optional[Any]
    recognizedVat: Optional[float]
    vat: Optional[float]
    vatPosition: Optional[Any]
    recognizedAmount: Optional[float]
    amount: Optional[float]
    amountPosition: Optional[Any]
    recognizedCountryCode: Optional[Any]
    countryCodePosition: Optional[Any]
    recognizedCountryShortName: Optional[Any]
    countryShortNamePosition: Optional[Any]
    customsDeclaration: Optional[Any]
    recognizedCustomsDeclaration: Optional[Any]
    customsDeclarationPosition: Optional[Any]
    nomenclature: Optional[Any]
    potentialNomenclatures: Optional[List]
    unit: Optional[Any]


class Customer(BaseModel):
    id: Optional[str]
    name: Optional[str]
    shortName: Optional[str]
    inn: Optional[str]
    kpp: Optional[str]
    creatorId: Optional[Any]
    taxId: Optional[Any]
    country: Optional[Any]


class InnPosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class KppPosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class RecognizedSupplier(BaseModel):
    id: Optional[str]
    context: Optional[Any]
    name: Optional[Any]
    namePosition: Optional[Any]
    inn: Optional[str]
    innPosition: Optional[InnPosition]
    kpp: Optional[str]
    kppPosition: Optional[KppPosition]


class Supplier(BaseModel):
    id: Optional[str]
    name: Optional[str]
    shortName: Optional[str]
    inn: Optional[str]
    kpp: Optional[str]
    creatorId: Optional[Any]
    taxId: Optional[Any]
    country: Optional[Any]


class Creator1(BaseModel):
    id: Optional[str]
    email: Optional[str]
    surname: Optional[Any]
    name: Optional[Any]
    patronymic: Optional[Any]
    lang: Optional[str]


class SupplierPosition(BaseModel):
    leftX: Optional[int]
    topY: Optional[int]
    rightX: Optional[int]
    pageNumber: Optional[int]
    bottomY: Optional[int]


class Document(BaseModel):
    id: Optional[str]
    createdDate: Optional[str]
    recognitionTask: Optional[RecognitionTask1]
    space: Optional[Space1]
    type: Optional[str]
    incomplete: Optional[bool]
    lowQuality: Optional[bool]
    pages: Optional[List[Page]]
    items: Optional[List[Item]]
    recognizedNumber: Optional[str]
    number: Optional[str]
    numberContext: Optional[Any]
    numberPosition: Optional[Any]
    recognizedDate: Optional[str]
    date: Optional[str]
    dateContext: Optional[Any]
    datePosition: Optional[Any]
    recognizedCustomer: Optional[Any]
    customer: Optional[Customer]
    recognizedSupplier: Optional[RecognizedSupplier]
    recognizedSupplierAccountDetails: Optional[Any]
    supplier: Optional[Supplier]
    amountRowHeaderPosition: Optional[Any]
    amountRowPosition: Optional[Any]
    recognizedAmountWithoutVat: Optional[float]
    amountWithoutVat: Optional[Any]
    amountWithoutVatPosition: Optional[Any]
    recognizedVat: Optional[float]
    vat: Optional[float]
    vatPosition: Optional[Any]
    recognizedAmount: Optional[float]
    amount: Optional[float]
    amountPosition: Optional[Any]
    verified: Optional[bool]
    creator: Optional[Creator1]
    receiptQrPosition: Optional[Any]
    receiptData: Optional[Any]
    externalSystemInfos: Optional[List]
    parent: Optional[Any]
    children: Optional[List]
    clientData: Optional[Any]
    paymentOrderId: Optional[Any]
    foreign: Optional[bool]
    state: Optional[str]
    receiptState: Optional[Any]
    pageCount: Optional[int]
    uploaded: Optional[bool]
    latestExternalSystemUploadingTask: Optional[Any]
    isSeen: Optional[bool]
    isNew: Optional[bool]
    customerPosition: Optional[Any]
    supplierPosition: Optional[SupplierPosition]
    forSendingToEdi: Optional[bool]


class RecognitionTask(BaseModel):
    id: Optional[str]
    space: Optional[Space]
    state: Optional[str]
    creator: Optional[Creator]
    files: Optional[List[File]]
    createdDate: Optional[str]
    finishDate: Optional[str]
    source: Optional[str]
    clientData: Optional[Any]
    documents: Optional[List[Document]]
    additionalProcessing: Optional[bool]
    balanceCost: Optional[int]


class Model(BaseModel):
    result: Optional[bool]
    recognitionTask: Optional[RecognitionTask]
