import { FieldQuery } from '../../query/encoding';
/**
 * Finer grained data types that takes binning and timeUnit into account.
 */
export declare enum ExtendedType {
    Q,
    BIN_Q,
    T,
    /**
     * Time Unit Temporal Field with time scale.
     */
    TIMEUNIT_T,
    /**
     * Time Unit Temporal Field with ordinal scale.
     */
    TIMEUNIT_O,
    O,
    N,
    K,
    NONE
}
export declare const Q: ExtendedType;
export declare const BIN_Q: ExtendedType;
export declare const T: ExtendedType;
export declare const TIMEUNIT_T: ExtendedType;
export declare const TIMEUNIT_O: ExtendedType;
export declare const O: ExtendedType;
export declare const N: ExtendedType;
export declare const K: ExtendedType;
export declare const NONE: ExtendedType;
export declare function getExtendedType(fieldQ: FieldQuery): ExtendedType;
